# -*- coding: utf-8 -*-
"""
DataFrame 結構
"""
import pandas as pd
import numpy as np
#沒有Dict key 二緯陣列
l=[[i*j for j in range(1,5,1)] for i in range(1,4,1)]
df=pd.DataFrame(l) 
print(df);print(df.columns);print(df.index)


#有 Dict key 一緯Dict
l=dict(zip(list('ABCD'),[[3 for i in range(3)] for j in range(4)]))
df=pd.DataFrame(l)
print(df) ; print(df.columns) ; print(df.index)





        
    


