# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 12:12:11 2022

@author: Homa

"""
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint
from selenium import webdriver
result=requests.get("https://forums.ni.com/t5/forums/searchpage/tab/message?advanced=false&allow_punctuation=false&filter=location&location=category:discussion-forums&q=usb%206009")

## To make sure the website is accessible

print(result.status_code)
## To make sure we are scrapping the correct website
#print(result.headers)

src=result.content

## parse and process the source
soup=BeautifulSoup(src, 'lxml')
# Find all the links 

links=soup.find_all('a')
# for link in links:
#     if "USB-6009" in link.text:
#         print(link)
# #         print(link.attrs['href'])




# find all div class (contents of first member asking question)
Question1= soup.find_all('div',class_='lia-truncated-body-container lia-truncate-with-message-link')[0]
title1= soup.find_all('a',class_='page-link lia-link-navigation lia-custom-event')[0]

print(title1)
#print(Question1)
Question2= soup.find_all('div',class_='lia-truncated-body-container lia-truncate-with-message-link')[1]
title2= soup.find_all('a',class_='page-link lia-link-navigation lia-custom-event')[1]
Question3= soup.find_all('div',class_='lia-truncated-body-container lia-truncate-with-message-link')[2]
title3= soup.find_all('a',class_='page-link lia-link-navigation lia-custom-event')[2]
Question4= soup.find_all('div',class_='lia-truncated-body-container lia-truncate-with-message-link')[3]
title4= soup.find_all('a',class_='page-link lia-link-navigation lia-custom-event')[3]

#print(Question2)

data=[]   

Questions_list=[[Question1, title1] ,[Question2,title2],[Question3,title3]]

# # find all the titles regarding USB-6009
title1= soup.find_all('a',class_='page-link lia-link-navigation lia-custom-event')[0]

# print(title1.attrs['href'])
# pages = np.arange(1, 11, 1)
# url_collected=[]
## Creating a dataframe from the questions list above

Comment_df = pd.DataFrame(Questions_list, columns=['Question', 'title'])
## Display first 5 entries from dataframe

# ## Export dataframe into a CSV
Comment_df.to_csv('National_data.csv', sep=',', index=False)
