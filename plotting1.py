# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 13:52:09 2022

@author: vishn
"""
import pandas as pd
import matplotlib.pyplot as plt
import calendar
import numpy as np
all_data=pd.read_excel('selenium_card.xlsx')
all_data.head()
all_data['month']=all_data['Date'].str[3:5]
final_year=all_data['Date'].str[6:10]
#print(final_year)
final_months = all_data['month'].astype('int32')
#print(final_months)
months_names= final_months.apply(lambda x: calendar.month_abbr[x])
#print(months_names)
final_revenue=(all_data['price']/all_data['Quantity'])*1000
print(final_revenue)
#final_months=all_data.groupby('Quantity').sum()

final_quantity=all_data['Quantity']
final_price=all_data['price']


xpoints=np.array(final_quantity)
ypoints=np.array(final_price)
fig = plt.subplots(figsize =(10, 7))
plt.hist(xpoints)
#plt.hist2d(xpoints, ypoints)
plt.show()
plt.hist(ypoints)
plt.show()
zpoints=np.array(final_revenue)
kpoints=np.array(months_names)
plt.bar(kpoints,zpoints)