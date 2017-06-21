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

#################



#n_to_process=100000

df=pd.read_csv("frac_1.csv")

min_trips=df['trips'].min()

n_drivers=len(df['trips'])
print n_drivers

tot_trips=sum(df['trips'])
total_air=sum(df['n_air'])
total_small=sum(df['n_small'])

prob_air=float(total_air)/float(tot_trips)
prob_small=float(total_small)/float(tot_trips)
print prob_air, prob_small

f_air=[]
f_small=[]
for i, row in df.iterrows():
  f_air.append(float(row['n_air'])/float(row['trips']))
  f_small.append(float(row['n_small'])/float(row['trips']))

ss_air=min_trips*prob_air*(1-prob_air)
ss_small=min_trips*prob_small*(1-prob_small)

r_air=np.random.binomial(min_trips,prob_air,size=n_drivers)/float(min_trips)
r_air=np.sort(r_air)

r_small=np.random.binomial(min_trips,prob_small,size=n_drivers)/float(min_trips)
r_small=np.sort(r_small)

d_small=sorted(f_small)
d_air=sorted(f_air)



fig, ax=plt.subplots()
plt.subplot(2, 1, 1)
plt.plot(d_air)
plt.plot(r_air)
plt.xticks([0,8000,16000])
plt.title('Airport trip fractions')
         
plt.subplot(2, 1, 2)
plt.plot(d_small)
plt.plot(r_small)
plt.xticks([0,8000,16000])
plt.xlabel('drivers')
plt.title('Unpopular destination trip fractions')

fig.tight_layout()
fig.savefig('fractions',format='pdf')
'''
#################
fig,ax=plt.subplots()
plt.plot(gsf)
#plt.plot(t_arr)
#plt.plot(tarrP)
#plt.plot(tarrN)
plt.plot(blah)
plt.xlabel('drivers with more than '+str(int(min_trips))+' pickups')
plt.ylabel('f(dropoffs in unpopular NTAs)')
fig.tight_layout()
fig.savefig('unpopfraction',format='pdf')
#################

dat_hist=np.histogram(gsf, density=True, bins='fd')
blah_hist=np.histogram(blah, density=True, bins='fd')

space=np.linspace(0.,dat_hist[1].max(),50)

#print dat_hist[0]
#print dat_hist[1]
#################
fig,ax=plt.subplots()
plt.plot(0.5*(dat_hist[1][1:]+dat_hist[1][:-1]),dat_hist[0] )
plt.plot(space, 1/(2*sigsqr*np.pi)**(0.5)*np.exp(-(space-prob)**2/2./sigsqr))
#plt.plot(t_arr)
#plt.plot(tarrP)
#plt.plot(tarrN)
#plt.plot(0.5*(blah_hist[1][1:]+blah_hist[1][:-1]),blah_hist[0])
#plt.xlabel('drivers with more than '+str(int(min_trips))+' pickups')
#plt.ylabel('f(dropoffs in unpopular NTAs)')
fig.tight_layout()
fig.savefig('hist_hist',format='pdf')
#################
'''
sys.exit()
