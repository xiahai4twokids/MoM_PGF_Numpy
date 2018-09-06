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
    