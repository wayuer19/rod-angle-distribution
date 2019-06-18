#!/usr/bin/python
import math,sys,os,subprocess
import string               
import numpy

f = open('angle.xyz','r')
fout = open('angle.dat','w')

#input the number of coil and rod length (n and m), and the total number np
m = int(raw_input("the number of m: "))
lines = f.readlines()
np = int(lines[0])
nmol = int(np/m)

f.close()
f = open('angle.xyz','r')
#read all of the points
p = []
for lines in f.readlines()[2:]:
    line = lines[10:53]
    line = line.split()
    for i in range(3):
        line[0] = float(line[0])
        line[1] = float(line[1])
        line[2] = float(line[2])
    p.append(line)
f.close()

#transform the points into rods and the com of the rod
rods, coms = [],[]
for i in range(nmol):
    rod, com = [0,0,0],[0,0,0]  
    j = i*m
    k = j+m-1
    rod[0], rod[1], rod[2] = p[k][0]-p[j][0], p[k][1]-p[j][1], p[k][2]-p[j][2]
    com[0], com[1], com[2] = (p[k][0]+p[j][0])*0.5, (p[k][1]+p[j][1])*0.5, (p[k][2]+p[j][2])*0.5
    rods.append(rod)
    coms.append(com)

#calculate the included angle between rod and normal vector of the membrane
nvx,nvy,nvz = 0,0,1
for i in range(nmol):
    axb = nvx*rods[i][0] + nvy*rods[i][1] + nvz*rods[i][2]
    a = math.sqrt(pow(nvx,2) + pow(nvy,2) +pow(nvz,2))
    b = math.sqrt(pow(rods[i][0],2) + pow(rods[i][1],2) +pow(rods[i][2],2))
    cosab = abs(axb/(a*b))
    angle = 90-numpy.arccos(cosab)*180.0/numpy.pi
    print >> fout, coms[i][0],coms[i][1],angle


