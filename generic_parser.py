#!/usr/bin/env python

import os
import os.path as op
import pandas as pd
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import seaborn as sns
# 1. load a dataset from a file
# 2. "organize" that file, so we can access columns *or* rows of it easily
# 3. compute some "summary statisics" about the dataset
# 4. print those summary statistics
# 1. load a dataset
# 1a. accept arbitrary filename as argument
from argparse import ArgumentParser
parser = ArgumentParser(description = 'A CSV reader + stats maker')
parser.add_argument('csvfile',
                     type = str,
                     help = 'path to the input csv file.')

parsed_args = parser.parse_args()
my_csv_file = parsed_args.csvfile

assert op.isfile(my_csv_file), "Please give us a real file, thx"
print('woot, the file exists')


#*********************************************************
# Load data, Organize dataset and Add header to the dataframe
#*********************************************************

data = pd.read_csv(my_csv_file, sep='\s+|,', header=None, engine='python', 
                names = ['ID number', 'Diagnosis','Radius_M', 'Texture_M', 'Perimeter_M', 'Area_M','Smoothness_M', 'Compactness_M', 'Concavity_M', 'ConcavePoints_M', 'Symmetry_M', 'FractalDimension_M',
                         'Radius_SE', 'Texture_SE', 'Perimeter_SE', 'Area_SE','Smoothness_SE', 'Compactness_SE', 'Concavity_SE', 'ConcavePoints_SE', 'Symmetry_SE', 'FractalDimension_SE',
                         'Radius_W', 'Texture_W', 'Perimeter_W', 'Area_W','Smoothness_W', 'Compactness_W', 'Concavity_W', 'ConcavePoints_W', 'Symmetry_W', 'FractalDimension_W'])
data.drop(['ID number'], axis=1, inplace=True)
#print(data.head())
#print(data.shape)
#print(data.dtypes)
#print(data.info())
print(data.columns)
#print(data.corr())

# Find missing values
print('Missing values:\n{}'.format(data.isnull().sum()))
# Find duplicated records
print('\nNumber of duplicated records: {}'.format(data.duplicated().sum()))
# Find the unique values of 'diagnosis'
print('\nUnique values of "Diagnosis": {}'.format(data['Diagnosis'].unique()))


# Access any row
#print(data.iloc[:,3:5])

# Access any column
#print(data.iloc[32:35,:])

#Access any value
#print(data.iloc[6,7])

# Compute Mean and STD
#print(np.mean(data))
#print(np.std(data))

def plotHistogram(data):
      for i, column in enumerate(data.columns):
            plt.figure(i)
            plt.hist(data[column], bins = 'auto', alpha = 0.5, label = 'x')
            plt.savefig('Hist_{}.png'.format(column))
            #plt.show()

def plotScatter(data):
      i = 1
      columncount = len(data.columns)
      columncount = 4  # To avoid having so many scatter
      while i < columncount - 1:
            j = i + 1
            while j < columncount:
                  for iv, jv in zip(data.iloc[:, i], data.iloc[:, j]):
                        plt.scatter(x = iv, y = jv)
                  plt.savefig('Scatt_{}.png'.format(data.columns[i] + ' ' + data.columns[j]))
                  #plt.show()
                  j = j + 1
            i = i + 1
 
def plotHeatmap(data):

      features_mean = ['Radius_M', 'Texture_M', 'Perimeter_M', 'Area_M','Smoothness_M', 'Compactness_M', 'Concavity_M', 'ConcavePoints_M', 'Symmetry_M', 'FractalDimension_M']
      plt.figure(figsize=(15,15))
      heat = sns.heatmap(data[features_mean].corr(), vmax = 1, square = True, annot = True)
      figure = heat.get_figure()
      figure.savefig('Heat.png', dpi = 400)
      #plt.show()

plotHistogram(data)
plotHeatmap(data)
plotScatter(data)


