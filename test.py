# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 19:30:55 2020

@author: Admx
"""

import bs4
from bs4 import BeautifulSoup
import requests



def getSearchPageResult(soup):
    results = []
    for div in soup.find_all(name='div', attrs={'class':'jobsearch-SerpJobCard'}):
        print(div)



url = 'https://ca.indeed.com/jobs?q=customer+service&l=Ottawa%2C+ON'

page = requests.get(url)
print(page.text)

soup = BeautifulSoup(page.text, 'html.parser')


results = getSearchPageResult(soup)



def scrapSearchPage(html_content):
    '''
    Scrap search page to fetch job posting

    Returns
    -------
    None.

    '''
    
    