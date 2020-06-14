#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import necessary libraries
import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
import time


# In[2]:


#set driver path and browser
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


#set variable for news site
news_url = "https://mars.nasa.gov/news/"


# In[4]:


#direct splinter to news site
browser.visit(news_url)


# In[8]:


#use beautiful soup to read news html file
html = browser.html

soup = bs(html, 'html.parser')

# find the first article using the '"list text" class'
article = soup.find('div', class_="list_text")


# In[9]:


#contain article title and teaser_text in separate variables
title = article.find('a').text
paragraph = article.find('div', class_ = "article_teaser_body").text


# In[10]:


#find featured image on nasa image site
#set image url
image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"


# In[11]:


#use splinter to open chrome browser and beautiful soup to parse page
browser.visit(image_url)
html = browser.html
soup = bs(html, 'html.parser')


# In[17]:


#click the "FULL IMAGE" link to open a new page with the desired picture
image = soup.find('a', class_='button fancybox')
click = browser.links.find_by_partial_text('FULL IMAGE').click() 


# In[18]:


html = browser.html
soup = bs(html, 'html.parser')
img_html= soup.find('img', class_="fancybox-image")['src']


# In[19]:


featured_image_url = "https://www.jpl.nasa.gov/"+img_html


# In[20]:


featured_image_url


# In[ ]:





# In[21]:


twit_url = "https://twitter.com/MarsWxReport"


# In[22]:


#use splinter to open chrome browser and beautiful soup to parse page
browser.visit(twit_url)
time.sleep(10)


# In[23]:


html = browser.html
time.sleep(10)
soup = bs(html, 'html.parser')


# In[24]:


tweet = soup.find('div', class_='css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0').text


# In[25]:


tweet


# In[26]:


facts_url = "https://space-facts.com/mars/"


# In[27]:


browser.visit(facts_url)
html = browser.html
soup = bs(html, 'html.parser')


# In[28]:


table = soup.find('table', class_= 'tablepress tablepress-id-p-mars')
table_rows = table.find_all('tr')


# In[29]:


i = []
for tr in table_rows:
    td = tr.find_all('td')
    row = [tr.text for tr in td]
    i.append(row)


# In[30]:


fact_frame = pd.DataFrame(i)


# In[31]:


html_table = fact_frame.to_html()
html_table


# In[32]:


hemi_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'


# In[33]:


browser.visit(hemi_url)
html = browser.html
soup = bs(html, 'html.parser')


# In[ ]:





# In[34]:


links = soup.find_all('a', class_='itemLink product-item')
links
# viking = browser.click_link_by_partial_text('Enhanced') 
# browser.execute_script("$('body').empty()")
# cerberus_element = soup.find('img', class_ ='wide-image')['src']


# In[62]:


i=0
title_list = []
url_list = []   
    
# Parse results and scrape titles and img links
astro_results = soup.find_all('div',class_="description")
for result in astro_results:
    #Add title to dictionary
    title = result.h3.text
    title_list.append(title)
    #Add url for full size image to dictionary
    browser.visit("https://astrogeology.usgs.gov/" + result.a['href'])
    nested_html = browser.html
    nested_soup = bs(nested_html, 'html.parser')
    nested_results = nested_soup.find('img',class_="wide-image")['src']
    url_list.append("https://astrogeology.usgs.gov/" + nested_results)


# In[100]:


tuples = list(zip(title_list, url_list))
new_df = pd.DataFrame(tuples)
renamed = new_df.rename(columns={0:'title',1:"image"})
dict = renamed.to_dict('records')


# In[102]:


dict


# In[50]:





# In[ ]:





# In[ ]:





# In[ ]:




