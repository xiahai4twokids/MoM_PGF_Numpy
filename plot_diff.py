# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 14:31:02 2018

@author: 913
"""
# In[]
import os
try:
    os.mkdir('result')
except Exception as e:
    print e
try: 
    os.mkdir('tempData')
except Exception as e:
    print e

# In[]

import pickle
#from multiprocessing import Pool as ProgPool

from mom_solver import Solution
from mom_solver import Parameters

name = "butterfly"

ID_sim_dir,details_sim_dir = Solution.simulator(filename=Parameters.Filename(name),\
                                                solverPar=Parameters.SolverPar('dir_dgf_free'))
with open('result/%s.txt'%ID_sim_dir,'w') as f:
    print ID_sim_dir
    pickle.dump(details_sim_dir,f)

# In[]
import matplotlib.pylab as plt
import numpy as np

rCSPar = Parameters.RCSPar()
if 'theta'==rCSPar.whichPlan:
    ## theta-plan
    plt.figure()
    plt.plot(details_sim_dir['theta'][:,0],10*np.log10(\
             details_sim_dir['f_h'][:,0]),label='h')
    plt.plot(details_sim_dir['theta'][:,0],10*np.log10(\
             details_sim_dir['f_e'][:,0]),label='e')
    plt.legend(fontsize=14)
    plt.xlabel('$\phi$',fontsize=14)
    plt.ylabel('RCS dBsm',fontsize=14)
    xlabel = np.linspace(0,np.pi,7)
    plt.xticks(xlabel,\
               np.array(xlabel*180/np.pi,dtype=int), \
               fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid()
    plt.show()
else:
    # phi-plan
    plt.figure()
    plt.plot(details_sim_dir['phi'][0,:],10*np.log10(\
             details_sim_dir['f_h'][0,:]),\
             label = "h")
    plt.plot(details_sim_dir['phi'][0,::],10*np.log10(\
             details_sim_dir['f_e'][0,:]),\
             label = 'e')
    plt.legend(fontsize=14)
    plt.xlabel('$\phi$',fontsize=14)
    plt.ylabel('RCS dBsm',fontsize=14)
    xlabel = np.linspace(0,np.pi,7)
    plt.xticks(xlabel,\
               np.array(xlabel*180/np.pi,dtype=int), \
               fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid()
    plt.show()
