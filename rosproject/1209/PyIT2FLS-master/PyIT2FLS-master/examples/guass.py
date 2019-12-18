#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 15 02:40:21 2019

@author: arslan
"""

from pyit2fls import IT2FLS, IT2FS_Gaussian_UncertStd, IT2FS_plot, \
                     min_t_norm, max_s_norm, TR_plot, crisp
from pyit2fls import IT2FS, trapezoid_mf, tri_mf,zero_mf
from numpy import linspace

#domain = linspace(0., 1., 100)
domain = linspace(-1., 1., 100)

NB = IT2FS_Gaussian_UncertStd(domain, [0,0.25, 0.05])

IT2FS_plot(NB,  filename="1")
# IT2FS_plot(NB, NS, PS,PB, legends=["NB", "NS", "PS","PB"], filename="asb(x1,x2)_ex_sets")




