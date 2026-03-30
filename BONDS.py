# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 15:13:41 2026

@author: Mukuka Noward Mfula 
"""
#functions to be used
import matplotlib.pyplot as plt
import pandas as pd
#reading csv file into dataframe
bonds = pd.read_csv("BONDS.csv")
#creating variable true value
bonds["true_value"] = bonds["CYR "] - bonds["INFLATION RATE"]
#describing the data
print(bonds.describe())
#plotting the first graph
plt.figure(figsize=(10,10))
plt.plot(bonds["DATE"],bonds["CYR "], label = "CUTOFF YIELD RATE", alpha=0.8)
plt.plot(bonds["DATE"],bonds["INFLATION RATE"] ,label="INFLATION",alpha=0.8)
plt.xlabel("DATE")
plt.ylabel("Percentage")
plt.title("CUTOFF YIELD VS INFLATION")
plt.xticks(rotation=100)
plt.legend()
plt.show()
#plotting the second graph
plt.figure(figsize=(10,10))
plt.plot(bonds["DATE"],bonds["true_value"])
plt.xlabel("DATE")
plt.ylabel("Percentage")
plt.title("TRUE VALUE")
plt.xticks(rotation=100)
plt.legend()
plt.show()