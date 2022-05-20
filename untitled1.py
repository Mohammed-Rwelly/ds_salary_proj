# -*- coding: utf-8 -*-
"""
Created on Wed May 18 14:27:28 2022

@author: Mohameed
"""
import glassdoor_scraper as gs
import pandas as pd 
path="C:/Users/Mohameed/Documents/ds_salary_proj/chromedriver"
df = gs.get_jobs('data scientist',15,False,path,200)