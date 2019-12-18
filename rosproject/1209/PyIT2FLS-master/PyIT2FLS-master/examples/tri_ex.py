#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 15 02:40:21 2019

@author: arslan
"""

from pyit2fls import IT2FLS, IT2FS_Gaussian_UncertStd, IT2FS_plot, \
                     min_t_norm, max_s_norm, TR_plot, crisp
from pyit2fls import IT2FS, trapezoid_mf, tri_mf
from numpy import linspace

domain = linspace(0., 1., 100)
Small = IT2FS(domain,
              tri_mf, [0, 0, 0.5, 1],
              tri_mf, [0, 0, 0.5, 0.8],
              )
Small.plot(filename="Small")
Medium = IT2FS(domain,
              tri_mf, [0, 0.5, 1., 1.],
              tri_mf, [0.1, 0.5, 0.9, 0.8],
              )
Medium.plot(filename="Medium")
Large = IT2FS(domain,
              tri_mf, [0, 0.5, 1., 1.],
              tri_mf, [0.1, 0.5, 0.9, 0.8],
              )
Large.plot(filename="Large")


S = IT2FS_Gaussian_UncertStd(domain, [0, 0.15, 0.1])
M = IT2FS_Gaussian_UncertStd(domain, [0.5, 0.15, 0.1])
L = IT2FS_Gaussian_UncertStd(domain, [1., 0.15, 0.1])
IT2FS_plot(S, M, L, legends=["S", "M", "L"], filename="y1_ex_sets")

myIT2FLS = IT2FLS()
myIT2FLS.add_input_variable("x1")
myIT2FLS.add_input_variable("x2")
myIT2FLS.add_output_variable("y1")
#myIT2FLS.add_output_variable("y2")

myIT2FLS.add_rule([("x1", Small), ("x2", Small)], [("y1", S)])
myIT2FLS.add_rule([("x1", Small), ("x2", Medium)], [("y1", S)])
myIT2FLS.add_rule([("x1", Small), ("x2", Large)], [("y1", M)])

myIT2FLS.add_rule([("x1", Medium), ("x2", Small)], [("y1", S)])
myIT2FLS.add_rule([("x1", Medium), ("x2", Medium)], [("y1", M)])
myIT2FLS.add_rule([("x1", Medium), ("x2", Large)], [("y1", L)])

myIT2FLS.add_rule([("x1", Large), ("x2", Small)], [("y1", M)])
myIT2FLS.add_rule([("x1", Large), ("x2", Medium)], [("y1", L)])
myIT2FLS.add_rule([("x1", Large), ("x2", Large)], [("y1", L)])

it2out, tr = myIT2FLS.evaluate({"x1":0.8, "x2":0.4}, min_t_norm, max_s_norm, domain)

it2out["y1"].plot(filename="y1_out")
TR_plot(domain, tr["y1"], filename="y1_tr")
print(crisp(tr["y1"]))




