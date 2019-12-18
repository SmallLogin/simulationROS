#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 15 02:40:21 2019

@author: arslan
"""

from pyit2fls import IT2FLS, IT2FS_Gaussian_UncertStd, IT2FS_plot, \
                     min_t_norm, max_s_norm, TR_plot, crisp
from numpy import linspace

#domain = linspace(0., 1., 100)
domain = linspace(-1., 1., 100)
'''
Small = IT2FS_Gaussian_UncertStd(domain, [0, 0.15, 0.1])
Medium = IT2FS_Gaussian_UncertStd(domain, [0.5, 0.15, 0.1])
Large = IT2FS_Gaussian_UncertStd(domain, [1., 0.15, 0.1])
'''
NS = IT2FS_Gaussian_UncertStd(domain, [-1., 0.15, 0.1])
NB = IT2FS_Gaussian_UncertStd(domain, [-0.5, 0.15, 0.1])
ZO = IT2FS_Gaussian_UncertStd(domain, [0., 0.15, 0.1])
PS = IT2FS_Gaussian_UncertStd(domain, [0.5, 0.15, 0.1])
PB = IT2FS_Gaussian_UncertStd(domain, [1., 0.15, 0.1])
IT2FS_plot(NS, NB, ZO,PS,PB, legends=["NS", "NB", "ZO", "PS", "PB"], filename="simp_ex_sets")

A1 = IT2FS_Gaussian_UncertStd(domain, [-1, 0.15, 0.1])
A2 = IT2FS_Gaussian_UncertStd(domain, [0, 0.15, 0.1])
A3 = IT2FS_Gaussian_UncertStd(domain, [1., 0.15, 0.1])
IT2FS_plot(A1, A2, A3, legends=["A1", "A2", "A3"], filename="y1_simp_ex_sets")

B1 = IT2FS_Gaussian_UncertStd(domain, [-1., 0.15, 0.1])
B2 = IT2FS_Gaussian_UncertStd(domain, [-0.25,0.15, 0.1])
B3 = IT2FS_Gaussian_UncertStd(domain, [-0.5, 0.15, 0.1])
B4 = IT2FS_Gaussian_UncertStd(domain, [0, 0.15, 0.1])
B5 = IT2FS_Gaussian_UncertStd(domain, [0.25, 0.15, 0.1])
B6 = IT2FS_Gaussian_UncertStd(domain, [0.5, 0.15, 0.1])
B7 = IT2FS_Gaussian_UncertStd(domain, [1., 0.15, 0.1])
IT2FS_plot(B1, B2, B3,B4,B5,B6,B7, legends=["B1", "B2", "B3", "B4", "B5", "B6", "B7"], filename="y2_simp_ex_sets")

myIT2FLS = IT2FLS()
myIT2FLS.add_input_variable("x1")
myIT2FLS.add_input_variable("x2")
myIT2FLS.add_output_variable("y1")
myIT2FLS.add_output_variable("y2")

myIT2FLS.add_rule([("x1", NS), ("x2", NS)], [("y1", A2), ("y2", B4)])
myIT2FLS.add_rule([("x1", NS), ("x2", NB)], [("y1", A2), ("y2", B4)])
myIT2FLS.add_rule([("x1", NS), ("x2", ZO)], [("y1", A2), ("y2", B3)])
myIT2FLS.add_rule([("x1", NS), ("x2", PS)], [("y1", A2), ("y2", B3)])
myIT2FLS.add_rule([("x1", NS), ("x2", PB)], [("y1", A2), ("y2", B2)])


myIT2FLS.add_rule([("x1", NB), ("x2", NS)], [("y1", A2), ("y2", B4)])
myIT2FLS.add_rule([("x1", NB), ("x2", NB)], [("y1", A1), ("y2", B4)])
myIT2FLS.add_rule([("x1", NB), ("x2", ZO)], [("y1", A1), ("y2", B3)])
myIT2FLS.add_rule([("x1", NB), ("x2", PS)], [("y1", A2), ("y2", B3)])
myIT2FLS.add_rule([("x1", NB), ("x2", PB)], [("y1", A1), ("y2", B2)])

myIT2FLS.add_rule([("x1", ZO), ("x2", NS)], [("y1", A2), ("y2", B7)])
myIT2FLS.add_rule([("x1", ZO), ("x2", NB)], [("y1", A1), ("y2", B7)])
myIT2FLS.add_rule([("x1", ZO), ("x2", ZO)], [("y1", A3), ("y2", B5)])
myIT2FLS.add_rule([("x1", ZO), ("x2", PS)], [("y1", A2), ("y2", B6)])
myIT2FLS.add_rule([("x1", ZO), ("x2", PB)], [("y1", A1), ("y2", B6)])

myIT2FLS.add_rule([("x1", PS), ("x2", NS)], [("y1", A2), ("y2", B2)])
myIT2FLS.add_rule([("x1", PS), ("x2", NB)], [("y1", A2), ("y2", B2)])
myIT2FLS.add_rule([("x1", PS), ("x2", ZO)], [("y1", A2), ("y2", B1)])
myIT2FLS.add_rule([("x1", PS), ("x2", PS)], [("y1", A2), ("y2", B1)])
myIT2FLS.add_rule([("x1", PS), ("x2", PB)], [("y1", A2), ("y2", B1)])

myIT2FLS.add_rule([("x1", PB), ("x2", NS)], [("y1", A2), ("y2", B2)])
myIT2FLS.add_rule([("x1", PB), ("x2", NB)], [("y1", A2), ("y2", B2)])
myIT2FLS.add_rule([("x1", PB), ("x2", ZO)], [("y1", A1), ("y2", B1)])
myIT2FLS.add_rule([("x1", PB), ("x2", PS)], [("y1", A2), ("y2", B1)])
myIT2FLS.add_rule([("x1", PB), ("x2", PB)], [("y1", A1), ("y2", B1)])

it2out, tr = myIT2FLS.evaluate({"x1":0, "x2":0}, min_t_norm, max_s_norm, domain)

it2out["y1"].plot(filename="y1_out")
TR_plot(domain, tr["y1"], filename="y1_tr")
print(crisp(tr["y1"]))

it2out["y2"].plot(filename="y2_out")
TR_plot(domain, tr["y2"], filename="y2_tr")
print(crisp(tr["y2"]))


