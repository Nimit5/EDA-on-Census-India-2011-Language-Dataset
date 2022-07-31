# Importing libraries 

import csv
import pandas as pd
import numpy as np
import warnings 
warnings.filterwarnings('ignore')

# Using C-08 Educational Level By Age And Sex For Population Age 7 And Above File
df=pd.read_excel('DDW-0000C-08.xlsx')

df.rename(columns={'Unnamed: 1':'State Code','Unnamed: 3':'Name','Unnamed: 4':'Total/Rural/Urban','C-8  EDUCATIONAL LEVEL BY AGE AND SEX FOR POPULATION AGE 7 AND ABOVE - 2011':'Age_Grp','Unnamed: 9' :'Illiterate','Unnamed: 12' :'Literate','Unnamed: 18' :'Literate but below primary','Unnamed: 21' :'Primary but below middle','Unnamed: 24' :'Middle but below matric/secondary','Unnamed: 27' :'Matric/Secondary','Unnamed: 30' :'Higher secondary/Intermediate/Pre-University/Senior secondary','Unnamed: 33' :'Non-technical diploma or certificate not equal to degree','Unnamed: 36' :'Technical diploma or certificate not equal to degree','Unnamed: 39' :'Graduate and above'}, inplace=True)

df=df[(df["Total/Rural/Urban"]=="Total") & (df["Age_Grp"]=='All ages')]

df['Matric/Secondary but below graduate']=df['Matric/Secondary']+df['Higher secondary/Intermediate/Pre-University/Senior secondary']+df['Non-technical diploma or certificate not equal to degree']+df['Technical diploma or certificate not equal to degree']

df=df[['State Code','Name','Illiterate','Literate','Literate but below primary','Primary but below middle','Middle but below matric/secondary','Graduate and above','Matric/Secondary but below graduate']]

df=df.melt(id_vars=["State Code", "Name"], var_name="literacy-group", value_name="population")

language_data= pd.read_excel('DDW-C19-0000.xlsx')

language_data=language_data.loc[(language_data['Unnamed: 3'] == 'Total' ) & ((language_data['Unnamed: 4'] == 'Middle but below matric/secondary') |(language_data['Unnamed: 4'] == 'Literate') | (language_data['Unnamed: 4'] == 'Literate but below primary') |(language_data['Unnamed: 4'] == 'Illiterate') | (language_data['Unnamed: 4'] == 'Primary but below middle') | (language_data['Unnamed: 4'] == 'Matric/Secondary but below graduate') | (language_data['Unnamed: 4'] == 'Graduate and above'))]

language_data.rename(columns={'C-19 POPULATION BY BILINGUALISM, TRILINGUALISM, EDUCATIONAL LEVEL AND SEX':'State Code','Unnamed: 2':'Name','Unnamed: 4':'literacy-group','Unnamed: 8':'Third language'}, inplace=True)

language_data=language_data[['State Code','Name','literacy-group','Third language']]


result=pd.merge(language_data,df,on=['State Code','literacy-group'])

result['Three or more']=(result['Third language']/result['population'])*100

result=result[['State Code','Name_x','literacy-group','Three or more']]

idx=result.groupby(['Name_x'])['Three or more'].transform(max)==result['Three or more']
result=result[idx]

result=result.rename(columns={'State Code':'state/ut','Three or more':'percentage'})

result=result.reset_index()
result.drop('index',axis=1,inplace=True)

result=result.drop('Name_x',axis=1)

result.to_csv('literacy-india.csv')

