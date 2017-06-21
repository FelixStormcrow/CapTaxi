#!/opt/local/bin/python2.7

import numpy as np
import math
import sys
import fiona
import shapely
from shapely.geometry import asShape
import pandas as pd
from scipy.spatial import distance

df=pd.read_csv("../trip_data/trip_data_1.csv",usecols=['hack_license', 'rate_code','pickup_datetime', 'pickup_longitude', 'pickup_latitude', 'dropoff_longitude', 'dropoff_latitude'])#, nrows=10000)

########


########
shapes={}


with fiona.open("../query.txt") as fiona_collection:
  num_NTA=len(fiona_collection)
  center_points=np.zeros([num_NTA+1,2])
  for shapefile_record in fiona_collection:
    shape=asShape( shapefile_record['geometry'])
    id=shapefile_record['properties']['OBJECTID']
    shapes[id]= shape
    center=shape.centroid
    center_points[id-1,:]=[center.x,center.y]
  center_points[num_NTA,:]=[-73.8740,40.7769] #LA GUARDIA!

driver=[]
pid=[]
did=[]
time=[]

for i,row in df.iterrows():
  if i%10000 == 0:  print "On iteration:",i
  driver.append(row['hack_license'])
  time.append(row['pickup_datetime'])
  plooking=True
  dlooking=True

  poi=shapely.geometry.Point(row['pickup_longitude'],row['pickup_latitude'])
  for i in distance.cdist([(row['pickup_longitude'],row['pickup_latitude'])],center_points)[0].argsort()[:3]:
    j=i+1
    if j == 196:
      pid.append(196)
      plooking=False
      break
    if shapes[j].contains(poi):
      pid.append(j)
      plooking=False
      break

  doi=shapely.geometry.Point(row['dropoff_longitude'],row['dropoff_latitude'])
  for i in distance.cdist([(row['dropoff_longitude'],row['dropoff_latitude'])],center_points)[0].argsort()[:3]:
    j=i+1
    if j == 196 or row['rate_code'] in [2,3]:
      did.append(196)
      dlooking=False
      break
    if shapes[j].contains(doi):
      did.append(j)
      dlooking=False
      break

  if plooking: pid.append(-1)
  if dlooking: did.append(-1)

print len(driver), len(time), len(pid), len(did)
good_df=pd.DataFrame({'hack_license':driver,'pid':pid,'did':did,'pickup_datetime':time})
good_df.to_csv('data_1_faster_exact.csv', mode='w')

sys.exit()
