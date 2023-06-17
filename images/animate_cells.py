# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 00:52:59 2023

@author: willi
"""

import numpy as np
from matplotlib.animation import FuncAnimation, PillowWriter
import matplotlib.pyplot as plt
from skimage.io import imread
vid = imread('D:/multiplexing_ML/p300_kdm5b_base_pb1.tif')
vid = np.moveaxis(np.array([vid[:,:,:,0], 2*vid[:,:,:,1], .1*vid[:,:,:,2]]), 0, -1)

def quantile_norm(movie, q ):  #quantile norm
    norm_movie = np.zeros(movie.shape)
    for i in range(movie.shape[-1]):
        chn_movie = movie[:,:,:,i]
        max_val = np.quantile(chn_movie, q)
        min_val = np.quantile(chn_movie, .005)
        norm_movie[:,:,:,i] = (chn_movie - min_val)/(max_val - min_val)
        
    norm_movie[norm_movie > 1] = 1
    norm_movie[norm_movie < 0] = 0
    return norm_movie

vid5 = quantile_norm(vid[:40], .99)
vid5[:,:,:,-1] = 0
fig,ax = plt.subplots(1,1,dpi=600)
a = ax.imshow(vid5[0])
ax.axis('off')

ind = [x for x in range(20)]  + [x for x in range(10,0,-1)] + [x for x in range(20,10,-1)]
def animate(i):
    
    print(ind[i])
    a.set_array(vid5[ind[i]])

    return [a]

ani = FuncAnimation(fig, animate, interval=50, blit=True, frames=40)
ani.save("cellsingle2.gif", writer=PillowWriter(fps=30), dpi=200, savefig_kwargs={"transparent": True})