# Importing libraries 

import csv
import pandas as pd
import numpy as np
import warnings 
warnings.filterwarnings('ignore')

# Using C-18 Population By Bilingualism, Trilingualism, Age And Sex File
df=pd.read_excel('DDW-C18-0000.xlsx')

# Rename columns
df.rename(columns={'C-18 POPULATION BY BILINGUALISM, TRILINGUALISM, AGE AND SEX':'state-code','Unnamed: 2':'State','Unnamed: 3': 'Total/Rural/Urban', 'Unnamed: 4' :'Age-group' ,'Unnamed: 5' :'Second Language Total' ,'Unnamed: 6' :'Second Language Males' ,'Unnamed: 7' :'Second Language Females' ,'Unnamed: 8' :'Third Language Total','Unnamed: 9' :'Third Language Males','Unnamed: 10' :'Third Language Females' }, inplace=True)

language_data=df[(df["Total/Rural/Urban"]=="Total") & (df["Age-group"]=="Total") ]

language_data=language_data[['state-code','State','Second Language Total','Third Language Total']]

df=pd.read_excel('DDW_PCA0000_2011_Indiastatedist.xlsx')

df=df[["Level","Name","TRU","TOT_P","TOT_M","TOT_F"]]

population_data=df[(df["Level"]=="STATE") & (df["TRU"]=="Total") ]

population_data.rename(columns={'Name':'State'}, inplace=True)

data=pd.merge(language_data,population_data,on='State')

data=data.drop(["Level","TRU","TOT_M","TOT_F"],axis=1)

data["one_lang"]=((data["TOT_P"]-data["Second Language Total"])/data["TOT_P"])*100
data["two_lang"]=((data["Second Language Total"]-data["Third Language Total"])/data["TOT_P"])*100
data["three_or_more_lang"]=(data["Third Language Total"]/data["TOT_P"])*100

def ratio_2_to_1():

    # Generate 2-to-1-ratio column
    data["2-to-1-ratio"]=data["two_lang"]/data["one_lang"]

    # Sorting 
    sorted_2_to_1=data.sort_values("2-to-1-ratio",ascending=False)

    # Writing output of ratio of exactly two languages to only one language in 2-to-1-ratio.csv file
    with open('2-to-1-ratio.csv','w') as out:
        csv_out=csv.writer(out)
        csv_out.writerow(['state-code','2-to-1-ratio'])

        # top-3 states (higher to lower ratio)
        for i in range(3):
            csv_out.writerow((sorted_2_to_1.iloc[i]['state-code'],sorted_2_to_1.iloc[i]["2-to-1-ratio"]))
    
        # worst-3 states (lower to higher ratio)
        for i in range(len(sorted_2_to_1)-1,len(sorted_2_to_1)-4,-1):
            csv_out.writerow((sorted_2_to_1.iloc[i]['state-code'],sorted_2_to_1.iloc[i]["2-to-1-ratio"]))

# Executing above functions to produce results

ratio_2_to_1()

