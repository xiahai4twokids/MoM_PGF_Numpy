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

name = "plane"

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
    plt.legend(fontsize=14)
    plt.xlabel('$\theta$ degree',fontsize=14)
    plt.ylabel('RCS dBsm',fontsize=14)
    xlabel = np.linspace(0,np.pi,7)
    plt.xticks(xlabel,\
               np.array(xlabel*180/np.pi,dtype=float), \
               fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid()
    plt.show()
    
    plt.plot(details_sim_dir['theta'][:,0],10*np.log10(\
             details_sim_dir['f_e'][:,0]\
             /(np.sin(details_sim_dir['theta'][:,0]))**2),label='e')
    plt.legend(fontsize=14)
    plt.xlabel('$\theta$ degree',fontsize=14)
    plt.ylabel('bi-RCS dBsm',fontsize=14)
    xlabel = np.linspace(0,np.pi,7)
    plt.xticks(xlabel,\
               np.array(xlabel*180/np.pi,dtype=float), \
               fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid()
    plt.show()
else:
    # phi-plan
    plt.figure()
    plt.plot(details_sim_dir['phi'][0,:],10*np.log10(\
             details_sim_dir['f_h'][0,:]),label = "h")
    plt.legend(fontsize=14)
    plt.xlabel('$\phi$ degree',fontsize=14)
    plt.ylabel('RCS dBsm',fontsize=14)
    xlabel = np.linspace(0,np.pi,7)
    plt.xticks(xlabel,\
               np.array(xlabel*180/np.pi,dtype=float), \
               fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid()
    plt.show()
    
    plt.plot(details_sim_dir['phi'][0,::],10*np.log10(\
             details_sim_dir['f_e'][0,:]),label = 'e')
    plt.legend(fontsize=14)
    plt.xlabel('$\phi$ degree',fontsize=14)
    plt.ylabel('RCS dBsm',fontsize=14)
    xlabel = np.linspace(0,np.pi,7)
    plt.xticks(xlabel,\
               np.array(xlabel*180/np.pi,dtype=float), \
               fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid()
    plt.show()

    plt.plot(details_sim_dir['phi'][0,::],10*np.log10(\
             details_sim_dir['f_e'][0,:]\
             /(np.sin(details_sim_dir['phi'][0,::]))**2),label = 'e')
    plt.legend(fontsize=14)
    plt.xlabel('$\phi$ degree',fontsize=14)
    plt.ylabel('bi-RCS dBsm',fontsize=14)
    xlabel = np.linspace(0,np.pi,7)
    plt.xticks(xlabel,\
               np.array(xlabel*180/np.pi,dtype=float), \
               fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid()
    plt.show()
    pass

