# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 12:34:36 2022

@author: vishn
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

import pandas as pd

driver = webdriver.Chrome(ChromeDriverManager().install())

DRIVER_PATH='C:\\Users\\vishn\\Downloads\\chromedriver_win32\\chromedriver.exe'


url = 'http://www.indianspices.com/marketing/price/domestic/daily-price8de9.html?v=archive&category=small'
driver.get(url)
final_list=[]

for j in range(0,1):
    
    
    sno=driver.find_elements_by_xpath('/html/body/div[2]/div/div[3]/div[2]/div[3]/div/div[3]/div/div/div[4]/table/tbody/tr/td[1]')
#print(sno)
    date=driver.find_elements_by_xpath('/html/body/div[2]/div/div[3]/div[2]/div[3]/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]')
    auctioneer_name=driver.find_elements_by_xpath('/html/body/div[2]/div/div[3]/div[2]/div[3]/div/div[3]/div/div/div[4]/table/tbody/tr/td[3]')
    quantity_sold=driver.find_elements_by_xpath('/html/body/div[2]/div/div[3]/div[2]/div[3]/div/div[3]/div/div/div[4]/table/tbody/tr/td[5]')
    price=driver.find_elements_by_xpath('/html/body/div[2]/div/div[3]/div[2]/div[3]/div/div[3]/div/div/div[4]/table/tbody/tr/td[7]')
    for i in range(len(auctioneer_name)):
        temp_data={'Sno':sno[i].text,
               'Date':date[i].text,
               'auctioneer':auctioneer_name[i].text,
               'Quantity':quantity_sold[i].text,
               'price':price[i].text}
        final_list.append(temp_data)
        print(final_list)
    df_frame=pd.DataFrame(final_list)
    n=2
    df2=df_frame.iloc[n:]
    #print(df2)
    df2.to_excel('selenium_card.xlsx',index=False)
    l=driver.find_element(By.CLASS_NAME,'pager-next')
    l.click()
    present_url=driver.current_url
    #print(present_url)
    url=present_url

        

    
    

