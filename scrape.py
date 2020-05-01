#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Pro tvoji informaci, kdybys chtel vedet vice co se deje: https://www.dataquest.io/blog/web-scraping-tutorial-python/


# In[2]:


# standartni library pro cmd a python requests
import requests
# HTML parser
from bs4 import BeautifulSoup
import pandas as pd


# In[11]:


# je to dynamicky nakonec, neobjevi se to v HTMl dokud neudelas expand
# ale pak se snazi najit informace z URL kterou jsem pouzil jako parameter
# da se to najit v Chrome Developer Tools
page = requests.get("https://www.avlka.cz/init/action/asynTransfer/drawLeague/?league=286")
soup = BeautifulSoup(page.content, 'html.parser')

#print(soup.prettify())


# In[4]:


# table muzes najit v nove sezone v Chrome Developer Tools
# hledame vsechny "tbody" tags
# na strance jsou 3 tables, my se zajimame o druhy => index 1
# najdeme vsechny cells v tom table
cells = soup.find_all('tbody')[1].find_all('td')

print(cells)

# containers pro nase hodnoty
rank = []
team = []
points = []
matches = []
success = []

for i in range(len(cells)):
    if i % 5 == 0:
        rank.append(cells[i].text.replace(".",""))
    elif i % 5 == 1:
        team.append(cells[i].text)
    elif i % 5 == 2:
        points.append(cells[i].text)
    elif i % 5 == 3:
        matches.append(cells[i].text)
    else:
        success.append(cells[i].text)


# In[10]:


# dataframe operations v pripade ze neznas: https://www.geeksforgeeks.org/python-pandas-dataframe/
lst = list(zip(rank,team,points,matches,success))

df = pd.DataFrame(lst, columns = ['rank','team','points','matches','success'])
print(df)

# mas bud lists nebo dataframe a to muzes automaticky poslat 

