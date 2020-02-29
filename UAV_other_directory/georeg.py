# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 22:56:41 2020

@author: KGaurav
"""


import math
import sympy as sy
import numpy as np
x,y,k,phi,ome,X,Y,Z,X0,Y0,Z0,x0,y0=sy.symbols('x y k phi ome X Y Z X0 Y0 Z0 x0 y0')

#f is focal length
f=151.876

# A,B,C,D,E are GCP
# format of input data ,point=[photo_x,photo_y,_ground_x,ground_y,ground_z]

A=[-53.845,65.230,6934.954,23961.100,160.136]
B=[104.50,68.324,7860.202,23941.560,152.653]
C=[4.701,-12.153,7261.078,23491.497,142.208]
D=[-61.372,-79.559,6836.650,23087.47,137.719]
E=[93.825,-62.060,7791.556,23166.680,138.827]

# para is list of initial guess for parameter in order X0,Y0,Z0,omega,phi,k
para=[7000,20000,1000,0,0,0,0,0]

#m11,m22...etc are elements of rotation matrix R
m11= sy.cos(k)*sy.cos(phi)
m12=-sy.sin(k)*sy.cos(phi)
m13=sy.sin(phi)
m21=sy.cos(k)*sy.sin(ome)*sy.sin(phi)+sy.sin(k)*sy.cos(ome)
m22=sy.cos(k)*sy.cos(ome)-sy.sin(k)*sy.sin(ome)*sy.sin(phi)
m23=-sy.sin(ome)*sy.cos(phi)
m31=sy.sin(k)*sy.sin(ome)-sy.cos(k)*sy.cos(ome)*sy.sin(phi)
m32=sy.sin(k)*sy.cos(ome)*sy.sin(phi)+sy.cos(k)*sy.sin(ome)
m33=sy.cos(ome)*sy.cos(phi)

p=m11*(X-X0)+m12*(Y-Y0)+m13*(Z-Z0)
q=m21*(X-X0)+m22*(Y-Y0)+m23*(Z-Z0)
r=m31*(X-X0)+m32*(Y-Y0)+m33*(Z-Z0)

Fx=x0-f*(p/r)
Fy=y0-f*(q/r)

#conversion into numerical algebra
argus=[x,y,X,Y,Z,X0,Y0,Z0,ome,phi,k,x0,y0]

dfxX=sy.lambdify((argus),sy.diff(Fx,X0))
dfxY=sy.lambdify((argus),sy.diff(Fx,Y0))
dfxZ=sy.lambdify((argus),sy.diff(Fx,Z0))
dfxome=sy.lambdify((argus),sy.diff(Fx,ome))
dfxphi=sy.lambdify((argus),sy.diff(Fx,phi))
dfxk=sy.lambdify((argus),sy.diff(Fx,k))
dfxx0=sy.lambdify((argus),sy.diff(Fx,x0))
dfxy0=sy.lambdify((argus),sy.diff(Fx,y0))

dfyX=sy.lambdify((argus),sy.diff(Fy,X0))
dfyY=sy.lambdify((argus),sy.diff(Fy,Y0))
dfyZ=sy.lambdify((argus),sy.diff(Fy,Z0))
dfyome=sy.lambdify((argus),sy.diff(Fy,ome))
dfyphi=sy.lambdify((argus),sy.diff(Fy,phi))
dfyk=sy.lambdify((argus),sy.diff(Fy,k))
dfyx0=sy.lambdify((argus),sy.diff(Fy,x0))
dfyy0=sy.lambdify((argus),sy.diff(Fy,y0))

Fx1=sy.lambdify((argus),Fx)
Fy1=sy.lambdify((argus),Fy)

count=0
while count<500:
#star to unpack value of list#
    desmat=[[dfxX(*(A+para)),dfxY(*(A+para)),dfxZ(*(A+para)),dfxome(*(A+para)),dfxphi(*(A+para)),dfxk(*(A+para)),dfxx0(*(A+para)),dfxy0(*(A+para))],[dfyX(*(A+para)),dfyY(*(A+para)),dfyZ(*(A+para)),dfyome(*(A+para)),dfyphi(*(A+para)),dfyk(*(A+para)),dfyx0(*(A+para)),dfyy0(*(A+para))],
             [dfxX(*(B+para)),dfxY(*(B+para)),dfxZ(*(B+para)),dfxome(*(B+para)),dfxphi(*(B+para)),dfxk(*(B+para)),dfxx0(*(B+para)),dfxy0(*(B+para))],[dfyX(*(B+para)),dfyY(*(B+para)),dfyZ(*(B+para)),dfyome(*(B+para)),dfyphi(*(B+para)),dfyk(*(B+para)),dfyx0(*(B+para)),dfyy0(*(B+para))],
             [dfxX(*(C+para)),dfxY(*(C+para)),dfxZ(*(C+para)),dfxome(*(C+para)),dfxphi(*(C+para)),dfxk(*(C+para)),dfxx0(*(C+para)),dfxy0(*(C+para))],[dfyX(*(C+para)),dfyY(*(C+para)),dfyZ(*(C+para)),dfyome(*(C+para)),dfyphi(*(C+para)),dfyk(*(C+para)),dfyx0(*(C+para)),dfyy0(*(C+para))],
             [dfxX(*(D+para)),dfxY(*(D+para)),dfxZ(*(D+para)),dfxome(*(D+para)),dfxphi(*(D+para)),dfxk(*(D+para)),dfxx0(*(D+para)),dfxy0(*(D+para))],[dfyX(*(D+para)),dfyY(*(D+para)),dfyZ(*(D+para)),dfyome(*(D+para)),dfyphi(*(D+para)),dfyk(*(D+para)),dfyx0(*(D+para)),dfyy0(*(D+para))],
             [dfxX(*(E+para)),dfxY(*(E+para)),dfxZ(*(E+para)),dfxome(*(E+para)),dfxphi(*(E+para)),dfxk(*(E+para)),dfxx0(*(E+para)),dfxy0(*(E+para))],[dfyX(*(E+para)),dfyY(*(E+para)),dfyZ(*(E+para)),dfyome(*(E+para)),dfyphi(*(E+para)),dfyk(*(E+para)),dfyx0(*(E+para)),dfyy0(*(E+para))]]
    
    L=[[A[0]-Fx1(*(A+para))],[A[1]-Fy1(*(A+para))],[B[0]-Fx1(*(B+para))],[B[1]-Fy1(*(B+para))],[C[0]-Fx1(*(C+para))],[C[1]-Fy1(*(C+para))],[D[0]-Fx1(*(D+para))],[D[1]-Fy1(*(D+para))],[E[0]-Fx1(*(E+para))],[E[1]-Fy1(*(E+para))]]
    
    #desmat is design matrix
    desmat=np.array(desmat)
    L=np.array(L)
    dX=np.dot(np.linalg.inv(np.dot(desmat.T,desmat)),(np.dot(desmat.T,L)))
    sigma_x= np.linalg.inv(np.dot(desmat.T,desmat))
    count+=1
    
    para[0]+=dX[0][0]
    para[1]+=dX[1][0]
    para[2]+=dX[2][0]
    para[3]+=dX[3][0]
    para[4]+=dX[4][0]
    para[5]+=dX[5][0]
    para[6]+=dX[6][0]
    para[7]+=dX[7][0]

dX=dX.tolist()
print(dX)
print(f'Value of X0= ',para[0])
print(f'Value of Y0= ',para[1])
print(f'Value of Z0= ',para[2])
print(f'Value of omega= ',para[3])
print(f'Value of phi= ',para[4])
print(f'Value of kappa= ',para[5])
print(f'Value of x0= ',para[6])
print(f'Value of y0= ',para[7])

