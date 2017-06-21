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
#mpl.use('Agg')
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

#generate small

small_cutoff=0.10

f = open('PID_COUNTS.csv',mode='r')
line=f.readline()
pid_count=np.array([int(i) for i in line.split(',')])
sort_pid_ind=pid_count.argsort()
cum_tot=np.cumsum(pid_count[sort_pid_ind])
small_trigger=np.searchsorted(cum_tot,cum_tot.max()*small_cutoff)
small_list=set([i+1 for i in sort_pid_ind[0:small_trigger]])
airport_quest=196 in small_list
if airport_quest:
  print 'Airports in small_list, be more restrictive'
  sys.exit()

#################

#generate airports

airport=[196]

#################

df=pd.read_csv('driver_didcount_1.csv')

##################

num_drivers=len(df['driver'])
DIDS=[i+1 for i in range(196)]

### determine fractions for drivers

driver=[]
tt=[]
n_air = []
n_small = []

min_drives=100

for index, dd in df.iterrows():
  if dd['trips'] >= min_drives: 
    driver.append(dd['driver'])
    tt.append(dd['trips'])
    n_air.append(sum([dd[str(i)] for i in DIDS if i in airport]))
    n_small.append(sum([dd[str(i)] for i in DIDS if i in small_list]))

fraction_df=pd.DataFrame({'driver':driver,'trips':tt,'n_air':n_air,'n_small':n_small})

fraction_df.to_csv('frac_1.csv',mode='w')



sys.exit()

