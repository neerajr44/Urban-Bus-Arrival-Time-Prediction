# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 23:44:08 2018

@author: Neeraj
"""

import numpy as np
#import pandas as pd

#df = pd.read_excel(r"C:\Users\Neeraj\KFbook.xlsx",sheetname='Sheet1')


def kf_predict(X,P,A,Q):
    X = A * X
    P = A * P * A
    return (X, P)

def kf_update(X,P,Z,H,R):
    IM = H*X
    IS = R + H*P*H
    K = P * H * (1/IS)
    X = X + (K*(Z-IM))
    P = P - (K*IS*K)
    return (X,P)

#Matrix Initialisation
X = 120.361
P = 1
Q = 0.01
R = 0.1
H = 1
Total_Time = [124.921,130.92,91.240,104.96]
A_list = [1.05,0.7,1.15,1.12]
Time_Elapsed = [4.4,3.56,4.2,3.72]


Z = list(np.array(np.multiply(Total_Time,A_list)) - np.array(Time_Elapsed))
#print(Z)


for i in range(len(Time_Elapsed)):
    print(A_list[i],P)
    [X,P] = kf_predict(X,P,A_list[i],Q)
    print(X)
    [X,P] = kf_update(X,P,Z[i],H,R)
    print(X,P)
    
print(X,P)
    