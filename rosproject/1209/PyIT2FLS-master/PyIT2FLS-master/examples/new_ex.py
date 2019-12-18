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
S = IT2FS_Gaussian_UncertStd(domain, [-1., 0.15, 0.1])
Z = IT2FS_Gaussian_UncertStd(domain, [0., 0.15, 0.1])
B = IT2FS_Gaussian_UncertStd(domain, [1., 0.15, 0.1])
IT2FS_plot(S, Z, B, legends=["S", "Z", "B"], filename="x1_simp_ex_sets")

SS = IT2FS_Gaussian_UncertStd(domain, [-1., 0.15, 0.1])
ZZ = IT2FS_Gaussian_UncertStd(domain, [0, 0.15, 0.1])
BB = IT2FS_Gaussian_UncertStd(domain, [1., 0.15, 0.1])
IT2FS_plot(SS, ZZ, BB, legends=["SS", "ZZ", "BB"], filename="x2_simp_ex_sets")

A1 = IT2FS_Gaussian_UncertStd(domain, [-1, 0.15, 0.1])
A2 = IT2FS_Gaussian_UncertStd(domain, [0, 0.15, 0.1])
A3 = IT2FS_Gaussian_UncertStd(domain, [1., 0.15, 0.1])
IT2FS_plot(A1, A2, A3, legends=["A1", "A2", "A3"], filename="y1_simp_ex_sets")

B1 = IT2FS_Gaussian_UncertStd(domain, [-1., 0.15, 0.1])
B2 = IT2FS_Gaussian_UncertStd(domain, [-0.75,0.15, 0.1])
B3 = IT2FS_Gaussian_UncertStd(domain, [-0.5, 0.15, 0.1])
B4 = IT2FS_Gaussian_UncertStd(domain, [-0.25, 0.15, 0.1])
B5 = IT2FS_Gaussian_UncertStd(domain, [0., 0.15, 0.1])
B6 = IT2FS_Gaussian_UncertStd(domain, [0.25, 0.15, 0.1])
B7 = IT2FS_Gaussian_UncertStd(domain, [0.5, 0.15, 0.1])
B8 = IT2FS_Gaussian_UncertStd(domain, [0.75, 0.15, 0.1])
B9 = IT2FS_Gaussian_UncertStd(domain, [1., 0.15, 0.1])
IT2FS_plot(B1, B2, B3,B4,B5,B6,B7, B8, B9, legends=["B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9"], filename="y2_simp_ex_sets")

myIT2FLS = IT2FLS()
myIT2FLS.add_input_variable("x1")
myIT2FLS.add_input_variable("x2")

myIT2FLS.add_output_variable("y1")
myIT2FLS.add_output_variable("y2")

myIT2FLS.add_rule([("x1", S), ("x2", S)], [("y1", A3)])
myIT2FLS.add_rule([("x1", S), ("x2", Z)], [("y1", A2)])
myIT2FLS.add_rule([("x1", S), ("x2", B)], [("y1", A1)])

myIT2FLS.add_rule([("x1", Z), ("x2", S)], [("y1", A2)])
myIT2FLS.add_rule([("x1", Z), ("x2", Z)], [("y1", A2)])
myIT2FLS.add_rule([("x1", Z), ("x2", B)], [("y1", A1)])

myIT2FLS.add_rule([("x1", B), ("x2", S)], [("y1", A1)])
myIT2FLS.add_rule([("x1", B), ("x2", Z)], [("y1", A1)])
myIT2FLS.add_rule([("x1", B), ("x2", B)], [("y1", A1)])


myIT2FLS.add_rule([("x1", SS), ("x2", SS)], [("y2", B4)])
myIT2FLS.add_rule([("x1", SS), ("x2", ZZ)], [("y2", B5)])
myIT2FLS.add_rule([("x1", SS), ("x2", BB)], [("y2", B6)])

myIT2FLS.add_rule([("x1", ZZ), ("x2", SS)], [("y2", B3)])
myIT2FLS.add_rule([("x1", ZZ), ("x2", ZZ)], [("y2", B9)])
myIT2FLS.add_rule([("x1", ZZ), ("x2", BB)], [("y2", B7)])

myIT2FLS.add_rule([("x1", BB), ("x2", SS)], [("y2", B2)])
myIT2FLS.add_rule([("x1", BB), ("x2", ZZ)], [("y2", B1)])
myIT2FLS.add_rule([("x1", BB), ("x2", BB)], [("y2", B8)])


it2out1, tr1 = myIT2FLS.evaluate({"x1":0.9, "x2":0.9}, min_t_norm, max_s_norm, domain)
it2out2, tr2 = myIT2FLS.evaluate({"x1":-0.8, "x2":0.8}, min_t_norm, max_s_norm, domain)

it2out1["y1"].plot(filename="y1_out")
TR_plot(domain, tr1["y1"], filename="y1_tr")
print(crisp(tr1["y1"]))

it2out2["y2"].plot(filename="y2_out")
TR_plot(domain, tr2["y2"], filename="y2_tr")
print(crisp(tr2["y2"]))


