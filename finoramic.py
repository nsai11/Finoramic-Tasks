#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 23:04:51 2020

@author: nsai
"""
import json
import subprocess
import sys

## opening json file from wd and storing the parsed json in data
f = open("/Users/nsai/Documents/finoramic.json")
data = json.load(f)

## Converting JSON to dictionary
dict1 = {}
for k in data["Dependencies"]:
    dict1 = k
    
## List for storing packages that have failed to download
failedPackage = []

##Shell script for downloading required dependencies with version specified
for k in dict1:
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install',k+"=="+dict1[k]])
    except subprocess.CalledProcessError:
        failedPackage.append(k)
        continue
        

##Printing Failed Packages
if(len(failedPackage) != 0):
    print("Failed package are : \n")        
    for i in failedPackage:
        print(i+"\n")
else:
    print("Success")
    
f.close()
