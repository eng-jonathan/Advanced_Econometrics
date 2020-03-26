# -*- coding: utf-8 -*-
"""
Spyder Editor

Title: Econ 387 Homework 3
Author: Jonathan Eng
Date: March 2, 2020
"""

import pandas as pd
import statsmodels.formula.api as smf

#1 & 3
Math_2006_2012_all = pd.read_csv('Math_2006_2012_All.csv')
Math_2013_2017_all = pd.read_csv('Math_2013_2017_All.csv')
English_2006_2012_all = pd.read_csv('English_2006_2012_All.csv')
English_2013_2017_all = pd.read_csv('English_2013_2017_All.csv')

def percent_as_ratio(x):
    df = pd.DataFrame({
        'PctLevel1':x['PctLevel1'],
        'PctLevel2':x['PctLevel2'],
        'PctLevel3':x['PctLevel3'],
        'PctLevel4':x['PctLevel4'],
        'PctLevel3and4':x['PctLevel3and4']
        })
    df = df.apply(pd.to_numeric, errors = 'coerce')
    df = df.dropna()
    return df/100
#2
math1_ratio = percent_as_ratio(Math_2006_2012_all)
math2_ratio = percent_as_ratio(Math_2013_2017_all)
english1_ratio = percent_as_ratio(English_2006_2012_all)
#English_2013_2017_All.csv already in Ratio form
english2_ratio =  percent_as_ratio(Math_2006_2012_all)*100

#4
def merge_dbn_year_grade(x, y):
    df1 = pd.DataFrame({'DBN':x['DBN'],  'Year':x['Year'],  'Grade':x['Grade'] })
    df2 = pd.DataFrame({'DBN':y['DBN'],  'Year':y['Year'],  'Grade':y['Grade'] })
    df3 = pd.merge(df1, df2)
    return df3

ME_2006_2017_all = merge_dbn_year_grade(English_2006_2012_all, Math_2006_2012_all)



#5
def get_borough(x):
    return x['DBN'].astype(str).str[2]
borough = get_borough(ME_2006_2017_all)
ME_2006_2017_all['Borough'] = borough

#6
print(ME_2006_2017_all.describe())

#7
def passing_score_summary(x, y):
    df = x.groupby(y)['MeanScaleScore'].describe()
    return df

exams = [Math_2006_2012_all, 
       Math_2013_2017_all, 
       English_2006_2012_all, 
       English_2013_2017_all]

for i in range (len(exams)):
    print(passing_score_summary(exams[i], 'Year'))
    print(passing_score_summary(exams[i], get_borough(exams[i])))
    print(passing_score_summary(exams[i], 'Grade'))
    
#8
def get_district(x):
    return x['DBN'].astype(str).str[:2]
    
district = get_district(ME_2006_2017_all)
ME_2006_2017_all['District'] = district

#9 & 10
for i in range(len(exams)):
    exams[i]['Borough'] = get_borough(exams[i])
    exams[i]['District'] = get_district(exams[i])
    
    mod1 = smf.ols (formula = 'PctLevel1 ~ Year + Borough + District', data = exams[i])
    mod2 = smf.ols (formula = 'PctLevel2 ~ Year + Borough + District', data = exams[i])
    mod3 = smf.ols (formula = 'PctLevel3 ~ Year + Borough + District', data = exams[i])
    mod4 = smf.ols (formula = 'PctLevel4 ~ Year + Borough + District', data = exams[i])

    mods = [mod1, mod2, mod3, mod4]
    for k in range(len(mods)):
        print(mods[k].fit().summary())














