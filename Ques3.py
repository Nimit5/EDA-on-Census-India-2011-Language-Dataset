# Importing libraries 

import csv
import pandas as pd
import numpy as np
import warnings 
from scipy import stats
warnings.filterwarnings('ignore')

df=pd.read_excel('DDW-C18-0000.xlsx')

df.rename(columns={'C-18 POPULATION BY BILINGUALISM, TRILINGUALISM, AGE AND SEX':'state-code','Unnamed: 2':'State','Unnamed: 3': 'TRU', 'Unnamed: 4' :'Age-group' ,'Unnamed: 5' :'Second Language','Unnamed: 8' :'Third Language'}, inplace=True)

df['State'] = df['State'].str.upper()

language_data_Urban=df[(df["TRU"]=="Urban") & (df["Age-group"]=="Total") ]
language_data_Rural=df[(df["TRU"]=="Rural") & (df["Age-group"]=="Total") ]

language_data_Rural=language_data_Rural[['state-code', 'State','Second Language','Third Language']]
language_data_Urban=language_data_Urban[['state-code', 'State','Second Language','Third Language']]

language_data_Rural=language_data_Rural.rename(columns={'Second Language':'Second Language R','Third Language':'Third Language R'})
language_data_Urban=language_data_Urban.rename(columns={'Second Language':'Second Language U','Third Language':'Third Language U'})

language_data=pd.merge(language_data_Urban,language_data_Rural,on=['state-code','State'])

df=pd.read_excel('DDW_PCA0000_2011_Indiastatedist.xlsx')

df=df[["Level","Name","TRU","TOT_P"]]

population_data_Urban=df[(df["Level"]!="DISTRICT") & (df["TRU"]=="Urban") ]
population_data_Rural=df[(df["Level"]!="DISTRICT") & (df["TRU"]=="Rural") ]

population_data_Urban=population_data_Urban[['Name','TOT_P']]
population_data_Rural=population_data_Rural[['Name','TOT_P']]

population_data_Urban.rename(columns={'Name':'State','TOT_P':'TOT U'}, inplace=True)
population_data_Rural.rename(columns={'Name':'State','TOT_P':'TOT R'}, inplace=True)

population_data_Urban['State'] = population_data_Urban['State'].str.upper()
population_data_Rural['State'] = population_data_Rural['State'].str.upper()

population_data_Urban=population_data_Urban.reset_index(drop=True)
population_data_Rural=population_data_Rural.reset_index(drop=True)

population_data=pd.merge(population_data_Rural,population_data_Urban,on=['State'])

data=pd.merge(population_data,language_data,on=['State'])

# Population ratio : Rural:Urban 
data['population-ratio']=data['TOT R']/data['TOT U']

data["ratio-one"]=(data["TOT R"]-data["Second Language R"])/(data["TOT U"]-data["Second Language U"])
data["ratio-two"]=(data["Second Language R"]-data["Third Language R"])/(data["Second Language U"]-data["Third Language U"])
data["ratio-three"]=data["Third Language R"]/data["Third Language U"]

data["rural-percent-one"]=((data["TOT R"]-data["Second Language R"])/data["TOT R"])*100
data["rural-percent-two"]=((data["Second Language R"]-data["Third Language R"])/data["TOT R"])*100
data["rural-percent-three"]=(data["Third Language R"]/data["TOT R"])*100

data["urban-percent-one"]=((data["TOT U"]-data["Second Language U"])/data["TOT U"])*100
data["urban-percent-two"]=((data["Second Language U"]-data["Third Language U"])/data["TOT U"])*100
data["urban-percent-three"]=(data["Third Language U"]/data["TOT U"])*100

data=data[['state-code', 'State','population-ratio', 'ratio-one', 'ratio-two', 'ratio-three',
       'rural-percent-one', 'rural-percent-two', 'rural-percent-three',
       'urban-percent-one', 'urban-percent-two', 'urban-percent-three']]

p_value=[]

for index, row in data.iterrows():
    vec1=np.array([row['ratio-one'],row['ratio-two'],row['ratio-three']])
    vec2=np.array([row['population-ratio'],row['population-ratio'],row['population-ratio']])
    t,p=stats.ttest_ind(vec1,vec2, equal_var=False)
    p_value.append(p)

data["p-value"]=p_value

df1=data[['state-code','urban-percent-one', 'rural-percent-one','p-value']]
df2=data[['state-code','urban-percent-two', 'rural-percent-two','p-value']]
df3=data[['state-code','urban-percent-three', 'rural-percent-three','p-value']]

df1=df1.rename(columns={'urban-percent-one':'urban-percentage','rural-percent-one':'rural-percentage'})
df2=df2.rename(columns={'urban-percent-two':'urban-percentage','rural-percent-two':'rural-percentage'})
df3=df3.rename(columns={'urban-percent-three':'urban-percentage','rural-percent-three':'rural-percentage'})

df1.to_csv('geography-india-a.csv', index=False)
df2.to_csv('geography-india-b.csv', index=False)
df3.to_csv('geography-india-c.csv', index=False)

