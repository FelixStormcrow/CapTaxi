#!/opt/local/bin/python2.7

import numpy as np
import math
import sys
import fiona
import shapely
from shapely.geometry import asShape
import pandas as pd
from scipy.spatial import distance

df=pd.read_csv("data_1_faster_exact.csv",usecols=['pid'])#,nrows=10)

tt = np.zeros(196,dtype=int)

########

for i, row in df.iterrows():
  if divmod(i,10000)[1]==0:
    print "On iteration:",i
  if row['pid'] !=-1: tt[row['pid']-1]+=int(1)

print tt

f = open('PID_COUNTS.csv', mode='w')
for i in range(195):
  f.write(str(tt[i])+',')
f.write(str(tt[195]))
f.close()

sys.exit()
