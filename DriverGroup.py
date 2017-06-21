#!/opt/local/bin/python2.7

import numpy as np
import math
import sys
import fiona
import shapely
from shapely.geometry import asShape
import pandas as pd
from collections import Counter
import cPickle as pickle

#################
'''
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib import rc
from matplotlib.ticker import MaxNLocator
from scipy import interpolate
rc('text', usetex=True)
#Colors
plt.rcParams['image.cmap'] = 'gist_heat'
#http://matplotlib.org/examples/color/colormaps_reference.html

mpl.rc('xtick',labelsize=24)
mpl.rc('ytick',labelsize=24)

font={'family':'normal',
  'weight':'bold',
    'size':24}

mpl.rc('font',**font)

mpl.rc('axes',linewidth=3)
mpl.rc('lines',linewidth=3)
'''
#################

df=pd.read_csv("data_1_faster_exact.csv",usecols=['hack_license', 'pid','did'])
priority=[21,22]

df21=df[df['pid']==21]
df22=df[df['pid']==22]
df=pd.concat([df21,df22])
df=df[df.did!=-1]


##################

driver_group = df.groupby('hack_license')

num_drivers=len(driver_group.groups.keys())

DIDS=[i+1 for i in range(196) ]

DID_counts={did:[] for did in DIDS}
trips=[]
driver=[]

for name, group in driver_group:
  driver.append(name)
  trips.append(group['did'].count())
  for did in DIDS:
    DID_counts[did].append(sum(group['did'] == did))

driver_data=pd.DataFrame({'driver':driver, 'trips':trips})
for did in DIDS:
  driver_data[did]=DID_counts[did]

driver_data.to_csv('driver_didcount_1.csv', mode='w')
                           
sys.exit()
