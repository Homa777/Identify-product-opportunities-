# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 22:46:44 2022

@author: Homa
"""
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re


############################Exractring the Questions ###########

# page = 1
# while page != 3:
#       url = f"https://forums.ni.com/t5/forums/searchpage/tab/message?filter=location&q=usb%206343&location=category:discussion-forums&page={page}&collapse_discussion=true"
#       print(url)
#       page = page + 1
# page=1  
page=1
question = []

while page< 2:
      url = f"https://forums.ni.com/t5/forums/searchpage/tab/message?filter=location&q=PCI&location=category:discussion-forums&page={page}&collapse_discussion=true"
      response = requests.get(url)
      html = response.content
      soup = BeautifulSoup(html, "lxml")
      
      for x in soup.find_all('div',class_='lia-truncated-body-container lia-truncate-with-message-link'):
          Question= x.get_text()
          print(Question)
          question.append(Question)
          Q = {"Questions": question}
            
      
      ## dataframe

          Comment_df = pd.DataFrame(Q)
          Comment_df.to_csv('National1_data.csv')
              
      page += 1
      
# # ############################## extracting titles #############################
# page=1 
    
# title=[]
# while page < 1000:
#       url = f"https://forums.ni.com/t5/forums/searchpage/tab/message?filter=location&q=usb%206343&location=category:discussion-forums&page={page}&collapse_discussion=true"
#       response = requests.get(url)
#       html = response.content
#       soup = BeautifulSoup(html, "lxml")
#       for y in soup.find_all('a', class_='page-link lia-link-navigation lia-custom-event'):
#           Title=y.get_text()
#           print (Title)
          
#           title.append(Title)
#           t= {"Title": title}
#           Comment_df = pd.DataFrame(t)
#           Comment_df.to_csv('National11_data.csv')

#       page += 1
# ################## Scraping number of replies & kudos for each document ###############

# page=1

# urls=[]
# kudos=[]

# replies=[]

# while page < 2:
#       url = f"https://forums.ni.com/t5/forums/searchpage/tab/message?filter=location&q=usb%206343&location=category:discussion-forums&page={page}&collapse_discussion=true"
#       result = requests.get(url)    

# ## To make sure the website is accessible

#       print(result.status_code)
# ## To make sure we are scrapping the correct website
# #print(result.headers)

#       src=result.content
# ## parse and process the source
#       soup=BeautifulSoup(src, 'lxml')


      
#       #Find all the links
#       for y in soup.find_all("a", class_="page-link lia-link-navigation lia-custom-event"):
#           href=y.attrs.get("href")
#           #print(href)
#           if "m-p" in href:
#               urls.append(href)
              
#       page+=1
                      
      
     

# for i in range(len(urls)):
#         urls[i]="https://forums.ni.com/" + urls[i]
#         response = requests.get(urls[i])
#         html = response.content
#         soup = BeautifulSoup(html, "lxml")

        # for p in soup.find_all("span", class_= ["MessagesPositionInThread",'aria-label'],limit=1):

        #       Replies=p.get_text()
        #       replies.append(Replies)
        #       R= {"number of replies": replies}
        #       Comment_df = pd.DataFrame(R)
        #       Comment_df.to_csv('National77_data.csv')      