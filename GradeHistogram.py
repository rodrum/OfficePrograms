# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 11:40:14 2018

@author: justin
"""
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
import csv

# Class name
class_name = 'Example Class'
# Input file name
input_file_name = 'test_grades.csv'
# Read CSV and just save percentages
percentages = []
with open(input_file_name, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=':')
    count = 0
    for row in spamreader:
        if count > 0:
            # row 5 is the one that has percentages
            # TODO: find the row automatically
            percentages.append(float(row[5].strip(' %')))
        count += 1
print('Percentages are: \n{}'.format(percentages))

# with open('Percents.txt', 'r+') as f: #change file name to your needs
#         lines = f.readlines()
#         newlines = [float(x[:-3]) for x in lines] #change value in brackets to fit your data

sdr = round(np.std(percentages),2)
mean = round(np.average(percentages),2)
median = round(np.median(percentages),2)
print('Standard error={0}, Mean={1}, Median={2}'.format(sdr, mean, median))

bins = 40 #set number of bins for histogram

plt.figure(figsize=(8,6))
plt.hist(percentages,bins,color='#39B21E',edgecolor='grey',linewidth=0.2,density='true')
plt.xlabel('Grade (%)')
plt.ylabel('Freq')
plt.title(class_name)
plt.xlim(0,100)
plt.ylim(0,0.09) #adjust ylim to your data

tx = 20 #set location of statistics text

plt.text(tx,0.04,'Std Dev =',horizontalalignment = 'right')
plt.text(tx,0.04,sdr)

plt.text(tx,0.05,'Median =',horizontalalignment = 'right')
plt.text(tx,0.05,median)

plt.text(tx,0.06,'Mean =',horizontalalignment = 'right')
plt.text(tx,0.06,mean)

plt.text(tx,0.03,'Bins =',horizontalalignment = 'right')
plt.text(tx,0.03,bins)

n = len(percentages)
plt.text(tx,0.02,'n =',horizontalalignment = 'right')
plt.text(tx,0.02,n)

x = np.arange(-1,101)
norm = mlab.normpdf(x,mean,sdr)

plt.plot(x,norm,color='Black')

plt.savefig('103Histogram.png')