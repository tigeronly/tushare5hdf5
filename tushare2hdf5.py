import tushare as ts
import pandas as pd
import h5py

tsdata = h5py.File('F:\\BaiduYunDownload\\machinelearning\\tsdata\\tsdata.h5','w')
Stock_Data=ts.get_k_data('300600')

print (tsdata)