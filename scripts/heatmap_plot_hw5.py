#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: wes
Created: Thu Sep 30 05:51:28 PDT 2021

Description: this code generates a 2D "heatmap" style plot using sample data that
is hard-coded into the code.

Inputs: none, all problem parameters are hard-coded.

Outputs: a plot showing the heatmap, displayed to the screen

Dependencies: matplotlib, numpy

Assumptions: Developed and Tested with Python 3.8.8 on MacOS 11.6
'''

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

threads_per_block = ['32', '64', '128', '256', '512', '1024'] # y axis, 6 of them
thread_blocks = ["1", "4", "16", "64", "256", "1024", "4096"] # x axis, 7 of them

# runtime = np.array([[977.9, 290.48, 74.95, 26.36, 5.22, 1.68, 0.94445],
#                 [494.12, 153.41, 41.1, 13.4, 3.03, 0.96659, 0.56294],
#                 [260.37, 85.44, 21.29, 5.28, 1.68, 0.6073, 0.48029],
#                 [171.23, 44.68, 11.84, 3.19, 0.96877, 0.57091, 0.45578],
#                 [103.08, 25.81, 6.89, 1.8, 0.66157, 0.50368, 0.46026],
#                 [58.83, 15.83, 4.09, 1.1, 0.639, 0.49501, 0.48371]])

# runtime = np.array([ [1.56, 1.56, 1.56, 1.56, 3.7, 14.76, 32.73],
#     [3.12, 3.12, 3.12, 3.12, 7.41, 29.06, 70.24],
#     [6.25, 6.25, 6.25, 6.25, 14.78, 55.1, 84.97],
#     [12.5, 12.5, 12.5, 12.49, 29.2, 71.17, 91.49],
#     [24.99, 24.99, 24.81, 24.78, 56.01, 84.91, 92.73],
#     [49.93, 48.83, 48.68, 48.56, 84.18, 91.09, 91.4]])

runtime = np.array([  [0.02,  0.06,  0.24,  0.69,  3.49, 10.89, 21.69],
    [0.04,  0.12,  0.44,  1.36,  6.02, 18.90, 34.69],
    [0.07,  0.21,  0.86,  3.46, 10.87, 30.97, 39.41],
    [0.11,  0.41,  1.54,  5.70, 18.81, 35.91, 40.48],
    [0.18,  0.70,  2.64, 10.11, 29.22, 38.44, 39.67],
    [0.31,  1.15,  4.45, 16.46, 32.54, 38.45, 37.65]])


fig, ax = plt.subplots()
im = ax.imshow(runtime, cmap="coolwarm")

# We want to show all ticks...
ax.set_xticks(np.arange(len(thread_blocks)))
ax.set_yticks(np.arange(len(threads_per_block)))
# ... and label them with the respective list entries
ax.set_xticklabels(thread_blocks)
ax.set_yticklabels(threads_per_block)

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
for i in range(len(threads_per_block)): # y axis
    for j in range(len(thread_blocks)): # x axis
        text = ax.text(j, i, runtime[i, j],
                       ha="center", va="center", color="k")

# ax.set_title("Runtime on GPU at Varying Block Size and Number of Blocks(ms)")
ax.set_title("sustained memory bandwidth percentage on GPU at Varying Block Size and Number of Blocks(%)")
ax.set_ylabel('The number of threads per block')
ax.set_xlabel('The number of blocks')
fig.colorbar(im, ax=ax)
fig.tight_layout()
plt.show()

# EOF
