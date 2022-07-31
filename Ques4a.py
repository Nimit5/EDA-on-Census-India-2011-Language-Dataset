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

def ratio_3_to_2():

    # Generate 3-to-2-ratio column
    data["3-to-2-ratio"]=data["three_or_more_lang"]/data["two_lang"]

    # Sorting 
    sorted_3_to_2=data.sort_values("3-to-2-ratio",ascending=False)

    # Writing output of ratio of population speaking three languages or more to exactly two languages in 3-to-2-ratio.csv file
    with open('3-to-2-ratio.csv','w') as out:
        csv_out=csv.writer(out)
        csv_out.writerow(['state-code','3-to-2-ratio'])

        # top-3 states (higher to lower ratio)
        for i in range(3):
            csv_out.writerow((sorted_3_to_2.iloc[i]['state-code'],sorted_3_to_2.iloc[i]["3-to-2-ratio"]))
    
        # worst-3 states (lower to higher ratio)
        for i in range(len(sorted_3_to_2)-1,len(sorted_3_to_2)-4,-1):
            csv_out.writerow((sorted_3_to_2.iloc[i]['state-code'],sorted_3_to_2.iloc[i]["3-to-2-ratio"]))

# Executing above functions to produce results

ratio_3_to_2()

