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
import numpy as np

#domain = linspace(0., 1., 100)
domain = linspace(-1., 1., 100)
'''
Small = IT2FS_Gaussian_UncertStd(domain, [0, 0.15, 0.1])
Medium = IT2FS_Gaussian_UncertStd(domain, [0.5, 0.15, 0.1])
Large = IT2FS_Gaussian_UncertStd(domain, [1., 0.15, 0.1])
IT2FS_plot(Small, Medium, Large, legends=["Small", "Medium", "large"], filename="asb(x1,x2)_ex_sets")

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
'''
NB = IT2FS_Gaussian_UncertStd(domain, [-1, 0.15, 0.1])
NS = IT2FS_Gaussian_UncertStd(domain, [-0.5, 0.15, 0.1])
ZO= IT2FS_Gaussian_UncertStd(domain, [0, 0.15, 0.1])
PS = IT2FS_Gaussian_UncertStd(domain, [0.5, 0.15, 0.1])
PB = IT2FS_Gaussian_UncertStd(domain, [1., 0.15, 0.1])
IT2FS_plot(NB, NS, ZO,PS,PB, legends=["NB", "NS", "ZO","PS","PB"], filename="asb(x1,x2)_ex_sets")

LVB = IT2FS_Gaussian_UncertStd(domain, [-0.875, 0.15, 0.1])
LB = IT2FS_Gaussian_UncertStd(domain, [-0.625, 0.15, 0.1])
LS= IT2FS_Gaussian_UncertStd(domain, [-0.375, 0.15, 0.1])
LVS = IT2FS_Gaussian_UncertStd(domain, [-0.125, 0.15, 0.1])
Z = IT2FS_Gaussian_UncertStd(domain, [0, 0.15, 0.1])
RVS = IT2FS_Gaussian_UncertStd(domain, [0.125, 0.15, 0.1])
RS = IT2FS_Gaussian_UncertStd(domain, [0.375, 0.15, 0.1])
RB= IT2FS_Gaussian_UncertStd(domain, [0.625, 0.15, 0.1])
RVB = IT2FS_Gaussian_UncertStd(domain, [0.875, 0.15, 0.1])
IT2FS_plot(LVB, LB, LS,LVS,Z,RVS,RS,RB,RVB, legends=["LVB", "LB", "LS","LVS","Z","RVS","RS","RB","RVB"], filename="y2_ex_sets")

myIT2FLS = IT2FLS()
myIT2FLS.add_input_variable("x1")
myIT2FLS.add_input_variable("x2")
#myIT2FLS.add_output_variable("y1")
myIT2FLS.add_output_variable("y2")

myIT2FLS.add_rule([("x1", NB), ("x2", NB)], [("y2", LS)])
myIT2FLS.add_rule([("x1", NB), ("x2", NS)], [("y2", LS)])
myIT2FLS.add_rule([("x1", NB), ("x2", ZO)], [("y2", LS)])
myIT2FLS.add_rule([("x1", NB), ("x2", PS)], [("y2", LB)])
myIT2FLS.add_rule([("x1", NB), ("x2", PB)], [("y2", LVB)])

myIT2FLS.add_rule([("x1", NS), ("x2", NB)], [("y2", LVS)])
myIT2FLS.add_rule([("x1", NS), ("x2", NS)], [("y2", LS)])
myIT2FLS.add_rule([("x1", NS), ("x2", ZO)], [("y2", LS)])
myIT2FLS.add_rule([("x1", NS), ("x2", PS)], [("y2", LVB)])
myIT2FLS.add_rule([("x1", NS), ("x2", PB)], [("y2", LVB)])

myIT2FLS.add_rule([("x1", ZO), ("x2", NB)], [("y2", Z)])
myIT2FLS.add_rule([("x1", ZO), ("x2", NS)], [("y2", Z)])
myIT2FLS.add_rule([("x1", ZO), ("x2", ZO)], [("y2", Z)])
myIT2FLS.add_rule([("x1", ZO), ("x2", PS)], [("y2", LVB)])
myIT2FLS.add_rule([("x1", ZO), ("x2", PB)], [("y2", LVB)])

myIT2FLS.add_rule([("x1", PS), ("x2", NB)], [("y2", RVS)])
myIT2FLS.add_rule([("x1", PS), ("x2", NS)], [("y2", RS)])
myIT2FLS.add_rule([("x1", PS), ("x2", ZO)], [("y2", RB)])
myIT2FLS.add_rule([("x1", PS), ("x2", PS)], [("y2", RVB)])
myIT2FLS.add_rule([("x1", PS), ("x2", PB)], [("y2", RVB)])

myIT2FLS.add_rule([("x1", PB), ("x2", NB)], [("y2", RS)])
myIT2FLS.add_rule([("x1", PB), ("x2", NS)], [("y2", RS)])
myIT2FLS.add_rule([("x1", PB), ("x2", ZO)], [("y2", RB)])
myIT2FLS.add_rule([("x1", PB), ("x2", PS)], [("y2", RB)])
myIT2FLS.add_rule([("x1", PB), ("x2", PB)], [("y2", RVB)])

it2out, tr = myIT2FLS.evaluate({"x1":0.8, "x2":0.6}, min_t_norm, max_s_norm, domain)
print(crisp(tr["y2"]))


# y=[]
# for i in range(-100,100,1):
#     for j in range(-100,100,1):
#         it2out, tr = myIT2FLS.evaluate({"x1":i/100, "x2":j/100}, min_t_norm, max_s_norm, domain)

#         #it2out["y1"].plot(filename="y1_out")
#         #TR_plot(domain, tr["y1"], filename="y1_tr")
#         print(crisp(tr["y2"]))
#         y.append(crisp(tr["y2"]))
# print(y)
# print(len(y))
# Y=np.array(y).reshape(200,200)
# print(Y)  #转换为二维矩阵
# print(np.shape(Y))  #12行1列
# np.savetxt('2.txt',Y)

# it2out, tr = myIT2FLS.evaluate({"x1":0.5, "x2":0.9}, min_t_norm, max_s_norm, domain)
#
# it2out["y2"].plot(filename="y2_out")
# TR_plot(domain, tr["y2"], filename="y2_tr")
# print(crisp(tr["y2"]))


