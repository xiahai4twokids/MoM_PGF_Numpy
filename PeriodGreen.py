# -*- coding: utf-8 -*-

# In[]

import numpy as np

wavenumber = np.pi*2.0

k = wavenumber
d = 1
h = 1
phi = 0

r = np.array([[0.1,0,0],\
                  [0.2,0,0],\
                  [0.3,0,0]])
rp = np.array([[0,0.5,0],\
                   [0,0.2,0]])

def pgf(r_0,rp_0,\
        k,d,phi,\
        nmax,mmax):
    n = np.linspace(-nmax,nmax,2*nmax+1)
    m = np.linspace(-mmax,mmax,2*mmax+1)
    
    
    ms,ns = np.meshgrid(m,n)
    rho_nm = [ns*d*np.cos(phi),ms*h+ns*d*np.sin(phi),np.zeros_like(ms)]
    rho_nm = np.array(rho_nm)
    rho_nm = rho_nm.transpose([1,2,0])
    
    

    
    r = r_0.reshape([1,-1,1,1,3])
    rp = rp_0.reshape([-1,1,1,1,3])
    
    r_rp_nm = r-rp-rho_nm
    R_nm = np.sum(r_rp_nm*r_rp_nm,axis=-1)
    
    k0 = np.array([0,0,1]).reshape([1,-1])
    a = np.exp(-1.j*k*R_nm)/R_nm
          
    b = np.exp( -1.j*\
                 np.sum(k0*rho_nm,axis=-1)\
                )
    
    #print a.shape
    #print b.shape
    
    c = a*b
    #print c
    
    return np.sum(\
                 np.sum(c,axis=-1),\
                       axis=-1)

a = pgf(r,rp, k,d,phi,1000,1000)
# In[]

# In[]

xs = np.linspace(100,1000,10)
bb = [np.mean(np.absolute(pgf(r,rp,k,d,phi,xx,xx)-a)/np.absolute(a))\
      for xx in xs]
bb = np.array(bb)

import matplotlib.pylab as plt
plt.figure()
plt.plot(xs,bb,'r-o',label="error")
plt.grid()
plt.xlabel('n/m_max')
plt.ylabel('error')
plt.xticks(xs)
plt.show()


