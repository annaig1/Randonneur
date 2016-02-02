# -*- coding: utf-8 -*-
"""
Created on Tue Feb 02 11:01:59 2016

Randonneur avec Python

@author: annaig
"""
import struct

def lire_header(path):
    f = open(path)
    lines=f.readlines()
    f.close()
    out={}
    for line in lines:
        if "=" in line:
            key = line.split("=")[0].split()[0]
            if key in ["lines", "samples"]:
              out[key] = int(line.split("=")[1])
    
    return out
    
def read_data(path):
    f = open(path, "rb")
    out = np.fromfile(f, dtype=np_float32)
    f.close()
    return out
    
header_path = "BossonsDEM_ll8m.hdr"
header = lire_header(header_path)

data_path = "BossonsDEM_ll8m"
data = read_data(data_path)

dx = 1.03112519e1
dy = 7.19750606e0
nx = header["samples"]
ny = header["lines"]
x = np.arange(header[nx]) * dx
y = (ny -np.arange(ny)) * dy
X, Y = np.meshgrid(x, y)
Z = data.reshape(ny, nx)

import matplotlib.pyplot as plt
import matplotlib

fig = plt.figure(0)
plt.clf()
ax = fig. add_subplot(1,1,1)
ax.set_aspect("equal")
plt.contourf(X, Y, Z, 100, cmap = matplotlib.cm.terrain)
cbar=plt.colorbar()
cbar.set_label("Altitude, $z$ [m]")
plt.contour(X, Y, Z, 20, colors= "k")
plt.grid()
plt.xlabel("Position, $x$ [m]")
plt.ylabel("Position, $y$ [m]")


from matplotlib.colors import LightSource
ls= LightSource(aedeg=0, altdeg=65)
rgb = ls.shade(Z, plt.cm.terrain)
plt.figure(1)
plt.imshow(rgb, extent=[0,x.max(),0,y.max()])
cbar = plt.colorbar(grad)
cbar.set_label("Altitude, $z$ [m]")
plt.xlabel("Position, $x$ [m]")
plt.ylabel("Position, $y$ [m]")

plt.show()