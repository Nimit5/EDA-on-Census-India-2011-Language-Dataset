# Importing libraries 

import csv
import pandas as pd
import numpy as np
import warnings 
from scipy import stats
warnings.filterwarnings('ignore')

df=pd.read_excel('DDW-C18-0000.xlsx')

df.rename(columns={'C-18 POPULATION BY BILINGUALISM, TRILINGUALISM, AGE AND SEX':'state-code','Unnamed: 2':'State','Unnamed: 3': 'Total/Rural/Urban', 'Unnamed: 4' :'Age-group' ,'Unnamed: 6' :'Second Language Males','Unnamed: 7' :'Second Language Females' ,'Unnamed: 9' :'Third Language Males','Unnamed: 10' :'Third Language Females' }, inplace=True)

language_data=df[(df["Total/Rural/Urban"]=="Total") & (df["Age-group"]=="Total") ]

language_data=language_data[['state-code','State','Second Language Males','Second Language Females','Third Language Males','Third Language Females']]

df=pd.read_excel('DDW_PCA0000_2011_Indiastatedist.xlsx')

df=df[["Level","Name","TRU","TOT_P","TOT_M","TOT_F"]]

population_data=df[(df["Level"]!="DISTRICT") & (df["TRU"]=="Total") ]

population_data.rename(columns={'Name':'State'}, inplace=True)

population_data['State']=population_data['State'].str.upper()

data=pd.merge(language_data,population_data,on='State')

data['population-ratio']=data['TOT_M']/data['TOT_F']

data["ratio-one"]=(data["TOT_M"]-data["Second Language Males"])/(data["TOT_F"]-data["Second Language Females"])
data["ratio-two"]=(data["Second Language Males"]-data["Third Language Males"])/(data["Second Language Females"]-data["Third Language Females"])
data["ratio-three"]=data["Third Language Males"]/data["Third Language Females"]

data["male-percent-one"]=((data["TOT_M"]-data["Second Language Males"])/data["TOT_M"])*100
data["male-percent-two"]=((data["Second Language Males"]-data["Third Language Males"])/data["TOT_M"])*100
data["male-percent-three"]=(data["Third Language Males"]/data["TOT_M"])*100

data["female-percent-one"]=((data["TOT_F"]-data["Second Language Females"])/data["TOT_F"])*100
data["female-percent-two"]=((data["Second Language Females"]-data["Third Language Females"])/data["TOT_F"])*100
data["female-percent-three"]=(data["Third Language Females"]/data["TOT_F"])*100

data=data[['state-code', 'State','population-ratio', 'ratio-one', 'ratio-two', 'ratio-three',
       'male-percent-one', 'male-percent-two', 'male-percent-three',
       'female-percent-one', 'female-percent-two', 'female-percent-three']]

p_value=[]

for index, row in data.iterrows():
    vec1=np.array([row['ratio-one'],row['ratio-two'],row['ratio-three']])
    vec2=np.array([row['population-ratio'],row['population-ratio'],row['population-ratio']])
    t,p=stats.ttest_ind(vec1,vec2, equal_var=False)
    p_value.append(p)

data["p-value"]=p_value

df1=data[['state-code','male-percent-one', 'female-percent-one','p-value']]
df2=data[['state-code','male-percent-two', 'female-percent-two','p-value']]
df3=data[['state-code','male-percent-three', 'female-percent-three','p-value']]

df1=df1.rename(columns={'male-percent-one':'male-percentage','female-percent-one':'female-percentage'})
df2=df2.rename(columns={'male-percent-two':'male-percentage','female-percent-two':'female-percentage'})
df3=df3.rename(columns={'male-percent-three':'male-percentage','female-percent-three':'female-percentage'})

df1.to_csv('gender-india-a.csv', index=False)
df2.to_csv('gender-india-b.csv', index=False)
df3.to_csv('gender-india-c.csv', index=False)
