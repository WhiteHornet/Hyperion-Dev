import pandas
import math
import glob
import os
import csv
import matplotlib.pyplot as plt
import numpy as np
#im not sure what else i can do with this code because tomorrow is my cut off day because i can do anything else other than that


df = pandas.read_csv('data1953.csv')
ds = pandas.read_csv('data2008.csv')
dg = pandas.read_csv('dataBoth.csv')

mean11 = df['BirthRate(Per1000 - 1953)'].mean()
mean12 = df['LifeExpectancy(1953)'].mean()
groupby_mean1 = df.groupby(['Countries', 'BirthRate(Per1000 - 1953)']).sum()
groupby_max1 = df.groupby(['Countries','LifeExpectancy(1953)' ]).sum()

mean21 = ds['BirthRate(Per1000 - 2008)'].mean()
mean22 = ds['LifeExpectancy(2008)'].mean()
groupby_mean12 = ds.groupby(['Countries','BirthRate(Per1000 - 2008)' ]).sum() 
groupby_max12 = ds.groupby(['Countries','LifeExpectancy(2008)' ]).sum()

groupby_mean31 = dg.groupby(['Countries','BirthRate(Per1000)']).sum()    
groupby_mean32 = dg.groupby(['Countries','LifeExpectancy']).sum()

final_mean = math.sqrt((mean21 - mean11)**2 + (mean22 - mean12)**2)

userinput = input("input csv file:")
if not ".csv" in userinput:
  userinput += ".csv"
data = pandas.read_csv(userinput)

rowcol = input("Column or row?: ")
if rowcol == "column":
  column = int(input("Which column?: "))
  result = data.iloc([column])
elif rowcol == "row":
  row = int(input("Which row?: "))
  result = data.iloc[[row]]
else:
  print("Invalid response.")

print(result)
print ('Birthrate, grouped by the Country: ' + str(final_mean))
plt.xlabel('BirthRate(Per1000) - red ')
plt.title('Country BirthRate and LifeExpectancy')
plt.ylabel('LifeExpectancy - blue')
plt.ylabel('both - green')
plt.scatter(groupby_mean31, groupby_mean32, c = "g")
plt.scatter("BirthRate(Per1000)","LifeExpectancy", c = "y")
plt.scatter(groupby_max1, groupby_max12, c = "b")
plt.scatter(groupby_mean1, groupby_mean12, c= "r")
plt.show()







          
        









