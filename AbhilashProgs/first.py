#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 11:02:08 2017

@author: abhilashsk
"""
#importing pandas, numpy and matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime


"""
Dataset loading section
"""

#Function for Data ingestion stage using read_csv
def readData():
    try:
        dataset=pd.read_csv('./Airplane_Crashes_and_Fatalities_Since_1908.csv') #storing the data in a DataFrame
        print("\nDataset loaded successfully.")
        return dataset
    except FileNotFoundError:
        print("\nThe file does not exist.")
    
    #print(crashds.head(2))
  
    
"""
Data cleaning section
"""

#Function for Data cleaning stage
def cleanData(dataset):
    print("\nCleaning data now...")
    del dataset['Summary']  #Summary column is dropped
    
    #removing invalid values
    ds1=dataset.isnull().any()
#    print(ds1)
    if True in ds1.values:  #if there are invalid value drop them
        print("\nThere are invalid values in the dataset. Deleting invalid values...")
        dataset=dataset.dropna()
        print("\nInvalid values have been dropped.\n")
#        ds1=dataset.isnull().any()
#        print(ds1)
    else:   #if there are no invalid values
        print("\nThere are no invalid values in the dataset.\n")
        
    #changing the format and type of values in Date column
    dataset['Date']=pd.to_datetime(dataset['Date'],format="%m/%d/%Y")
    
    print("\nDataset has been cleaned.")
    #returning dataset
    return dataset


"""
Data Transformation Section
"""

#Function to return columns of the dataset
def getColumns(dataset,col,rowStart,rowEnd):
    print("\nIn getColumns method....  ")
    return dataset[col].iloc[rowStart:rowEnd]

#Function to return dataset filtered by dates
def filterByDates(dataset,frm,to):
    print("\nIn filterByDate method....  ")
    filter_1=dataset['Date']>frm
    filter_2=dataset['Date']<to
    return dataset[filter_1 & filter_2]

#Function to return dataset filtered by Operator
def filterByOperator(dataset,operator):
    print("\nIn filterByOperator method....  ")
    filter_op=dataset['Operator'].str.contains(operator)
    return dataset[filter_op]



"""
Descriptive Statistics Section
"""
#Function to get dataset details
def desDataset(dataset,info):
    print("\nIn desDataset method....  ")
    if info=="shape":
        return dataset.shape

#Function to describe the columns
def desColumns(dataset,col):
    print("\nIn desColumns method....  ")
    desc=dataset[col].describe()
    return desc

#Function for displaying data regarding the data set
def defDataset(dataset):
    print("\nIn defDataset method....  ")
    #print(dataset.head())
    #print(dataset.tail())
    shape=dataset.shape
    columns=dataset.columns
    print("The Indices of the dataset: ",columns,"\nThe shape of dataset: ",shape)
    #dataset.plot(x='Operator',y='Fatalities',figsize=(15,10),kind='bar')


#Function to return column and rows of the dataset
def retData(dataset,cols,rows=0):   #cols will be a list of columns selected
    print("\nIn retData method....  ")
    columns=dataset.columns
    for x in columns:
        print(dataset[x])


#ds=readData()
#ds=cleanData(ds)
##print(ds.head(10))
#desColumns(ds,'Aboard')
