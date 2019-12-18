#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 20:23 2019
control Speed magnitude(v1)
@author: SmallLogo
"""

from pyit2fls import IT2FLS, IT2FS_Gaussian_UncertStd, IT2FS_plot, \
                     min_t_norm, max_s_norm, TR_plot, crisp
from pyit2fls import IT2FS, trapezoid_mf, tri_mf
from numpy import linspace
import numpy as np
def IT2FL_v1_fun(y):
    # print("chenggong")
    domain = linspace(-1, 1., 100)
    
    NB = IT2FS_Gaussian_UncertStd(domain, [-1, 0.15, 0.1])
    NS = IT2FS_Gaussian_UncertStd(domain, [-0.5, 0.15, 0.1])
    MM= IT2FS_Gaussian_UncertStd(domain, [0, 0.15, 0.1])
    PS = IT2FS_Gaussian_UncertStd(domain, [0.5, 0.15, 0.1])
    PB = IT2FS_Gaussian_UncertStd(domain, [1., 0.15, 0.1])
    # IT2FS_plot(NB, NS, MM,PS,PB, legends=["NB", "NS", "NN","PS","PB"], filename="v1_input_$y")

    BB = IT2FS_Gaussian_UncertStd(domain, [-1, 0.15, 0.1])
    BS= IT2FS_Gaussian_UncertStd(domain, [-0.5, 0.15, 0.1])
    ZO= IT2FS_Gaussian_UncertStd(domain, [0, 0.15, 0.1])
    GS = IT2FS_Gaussian_UncertStd(domain, [0.5, 0.15, 0.1])
    GB = IT2FS_Gaussian_UncertStd(domain, [1., 0.15, 0.1])
    # IT2FS_plot(GB,GS,ZO,BS,BB, legends=["GB", "GS", "ZO","BS","BB"], filename="V1_output")

    #输入和输出都只有一个，输入为y方向的偏离值，输出为速度大小即前进或者后退的快慢
    myIT2FLS = IT2FLS()
    myIT2FLS.add_input_variable("x1")
    
    myIT2FLS.add_output_variable("y1")
    

    myIT2FLS.add_rule([("x1", NB)], [("y1", GB)])
    myIT2FLS.add_rule([("x1", NS)], [("y1", GS)])
    myIT2FLS.add_rule([("x1", MM)], [("y1", ZO)])
    myIT2FLS.add_rule([("x1", PS)], [("y1", BS)])
    myIT2FLS.add_rule([("x1", PB)], [("y1", BB)])


    it2out, tr = myIT2FLS.evaluate({"x1":y}, min_t_norm, max_s_norm, domain)
    # it2out["y1"].plot(filename="y1_out")
    # TR_plot(domain, tr["y1"], filename="y1_tr")
    print("v1_output:",crisp(tr["y1"]))
    if crisp(tr["y1"]) <0:
        print("速度大小：后退",crisp(tr["y1"])*2)
    elif crisp(tr["y1"])==0:
        print("速度大小：0")
    else:
        print("速度大小：前进",crisp(tr["y1"])*2)
    

# y=[]
# for i in range(0,100,1):
#     for j in range(0,100,1):
#         it2out, tr = myIT2FLS.evaluate({"x1":i/100, "x2":j/100}, min_t_norm, max_s_norm, domain)

#         #it2out["y1"].plot(filename="y1_out")
#         #TR_plot(domain, tr["y1"], filename="y1_tr")
#         print(crisp(tr["y1"]))
#         y.append(crisp(tr["y1"]))
# print(y)
# print(len(y))
# Y=np.array(y).reshape(100,100)
# print(Y)  #转换为二维矩阵
# print(np.shape(Y))  #12行1列
# np.savetxt('1.txt',Y)





