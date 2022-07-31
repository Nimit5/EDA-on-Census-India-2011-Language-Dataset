# Importing libraries 

import csv
import pandas as pd
import numpy as np
import warnings 
warnings.filterwarnings('ignore')

df=pd.read_excel('DDW-C18-0000.xlsx')

df.rename(columns={'C-18 POPULATION BY BILINGUALISM, TRILINGUALISM, AGE AND SEX':'state-code','Unnamed: 2':'State','Unnamed: 3': 'Total/Rural/Urban', 'Unnamed: 4' :'Age-group' ,'Unnamed: 5' :'Second Language Total' ,'Unnamed: 6' :'Second Language Males' ,'Unnamed: 7' :'Second Language Females' ,'Unnamed: 8' :'Third Language Total','Unnamed: 9' :'Third Language Males','Unnamed: 10' :'Third Language Females' }, inplace=True)

language_data=df[(df["Total/Rural/Urban"]=="Total") & (df["Age-group"]=="Total") ]

language_data=language_data[['state-code','State','Second Language Total','Third Language Total']]

df=pd.read_excel('DDW_PCA0000_2011_Indiastatedist.xlsx')

df=df[["Level","Name","TRU","TOT_P","TOT_M","TOT_F"]]

population_data=df[(df["Level"]!="DISTRICT") & (df["TRU"]=="Total") ]

population_data.rename(columns={'Name':'State'}, inplace=True)

population_data['State'] = population_data['State'].str.upper()

data=pd.merge(language_data,population_data,on='State')

data["percent-one"]=((data["TOT_P"]-data["Second Language Total"])/data["TOT_P"])*100
data["percent-two"]=((data["Second Language Total"]-data["Third Language Total"])/data["TOT_P"])*100
data["percent-three"]=(data["Third Language Total"]/data["TOT_P"])*100

data=data.drop(["State","Second Language Total","Third Language Total","Level","TRU","TOT_P","TOT_M","TOT_F"],axis=1)

data.to_csv('percent-india.csv', index=False)
