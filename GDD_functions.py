#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def cleaner_copr(df):
    df1= df.rename(columns={'AirTC_1_Avg: COPR-15min, (∞C)' : 'Temp'})
    df1= df1.groupby(['Month','Day','Date'], as_index=False).agg({'Temp': ['min', 'max']})
    clean = {'Date': df1['Date'], 'Min' : df1['Temp']['min'], 'Max':df1['Temp']['max']}
    df_clean = pd.DataFrame(data= clean)
    df_clean['Mid']=(df_clean['Max']+df_clean['Min'])/2
    df_clean['GDD'] =(df_clean['Mid'] - 6)
    df_clean['Date']= pd.to_datetime(df1['Date'])
    df_clean = df_clean.sort_values('Date').reset_index(drop=True)
    return(df_clean)

def cleaner_air(df):
    df1= df.rename(columns={'AirTC_1_Avg: Airstrip-15min, (°C)' : 'Temp'})
    df1= df1.groupby(['Month','Day','Date'], as_index=False).agg({'Temp': ['min', 'max']})
    clean = {'Date': df1['Date'], 'Min' : df1['Temp']['min'], 'Max':df1['Temp']['max']}
    df_clean = pd.DataFrame(data= clean)
    df_clean['Mid']=(df_clean['Max']+df_clean['Min'])/2
    df_clean['GDD'] =(df_clean['Mid'] - 6)
    df_clean['Date']= pd.to_datetime(df1['Date'])
    df_clean = df_clean.sort_values('Date').reset_index(drop=True)
    return(df_clean)

def ndvi_cleaner(ndvi):
    ndvi= ndvi.rename(columns={'DateTime' : 'Date'})
    ndvi['Date']= pd.to_datetime(ndvi['Date'])
    ndvi = ndvi.sort_values('Date').reset_index(drop=True)
    return(ndvi)

def ndvi_thresh_date(df,filt):
    test= df[df['NDVI']>.4].reset_index(drop=True)
    return(test.Date[0])

def GDD_calc(df, date):
    
    #dff= filt_df[filt_df.Mid >= 6]
    dff2 =df[df.Date <date]
    #return(len(dff2))
    x=sum(dff2.GDD)
    return(x)

def clean_soil_air(df):
    df1 = df
    df1 =  df1.groupby(['Month','Day','Date'], as_index=False).mean()
    df1= df1[['Date', 'SMwfv']]
    df1['Date']= pd.to_datetime(df1['Date'])
    df_clean = df1.sort_values('Date').reset_index(drop=True)
    df_clean = df_clean.fillna(method='ffill')
    return(df_clean)