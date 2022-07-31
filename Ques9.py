# Importing libraries 

import csv
import pandas as pd
import numpy as np
import warnings 
warnings.filterwarnings('ignore')

# Using C-08 Educational Level By Age And Sex For Population Age 7 And Above File
df=pd.read_excel('DDW-0000C-08.xlsx')

df.rename(columns={'Unnamed: 1':'State Code','Unnamed: 3':'Name','Unnamed: 4':'Total/Rural/Urban','C-8  EDUCATIONAL LEVEL BY AGE AND SEX FOR POPULATION AGE 7 AND ABOVE - 2011':'Age_Grp','Unnamed: 10' :'Illiterate M','Unnamed: 11' :'Illiterate F','Unnamed: 13' :'Literate M','Unnamed: 14' :'Literate F','Unnamed: 19' :'Literate but below primary M','Unnamed: 20' :'Literate but below primary F','Unnamed: 22' :'Primary but below middle M','Unnamed: 23' :'Primary but below middle F','Unnamed: 25' :'Middle but below matric/secondary M','Unnamed: 26' :'Middle but below matric/secondary F','Unnamed: 28' :'Matric/Secondary M','Unnamed: 29' :'Matric/Secondary F','Unnamed: 31' :'Higher secondary/Intermediate/Pre-University/Senior secondary M','Unnamed: 32' :'Higher secondary/Intermediate/Pre-University/Senior secondary F','Unnamed: 34' :'Non-technical diploma or certificate not equal to degree M','Unnamed: 35' :'Non-technical diploma or certificate not equal to degree F','Unnamed: 37' :'Technical diploma or certificate not equal to degree M','Unnamed: 38' :'Technical diploma or certificate not equal to degree F','Unnamed: 40' :'Graduate and above M','Unnamed: 41' :'Graduate and above F'}, inplace=True)

df=df[(df["Total/Rural/Urban"]=="Total") & (df["Age_Grp"]=='All ages')]

df['Matric/Secondary but below graduate M']=df['Matric/Secondary M']+df['Higher secondary/Intermediate/Pre-University/Senior secondary M']+df['Non-technical diploma or certificate not equal to degree M']+df['Technical diploma or certificate not equal to degree M']
df['Matric/Secondary but below graduate F']=df['Matric/Secondary F']+df['Higher secondary/Intermediate/Pre-University/Senior secondary F']+df['Non-technical diploma or certificate not equal to degree F']+df['Technical diploma or certificate not equal to degree F']

df_males=df[['State Code','Name','Illiterate M','Literate M','Literate but below primary M','Primary but below middle M','Middle but below matric/secondary M','Graduate and above M','Matric/Secondary but below graduate M']]
df_females=df[['State Code','Name','Illiterate F','Literate F','Literate but below primary F','Primary but below middle F','Middle but below matric/secondary F','Graduate and above F','Matric/Secondary but below graduate F']]

df_males.rename(columns={'Illiterate M':'Illiterate','Literate M':'Literate','Literate but below primary M':'Literate but below primary','Primary but below middle M':'Primary but below middle','Middle but below matric/secondary M':'Middle but below matric/secondary','Graduate and above M':'Graduate and above','Matric/Secondary but below graduate M':'Matric/Secondary but below graduate'}, inplace=True)

df_females.rename(columns={'Illiterate F':'Illiterate','Literate F':'Literate','Literate but below primary F':'Literate but below primary','Primary but below middle F':'Primary but below middle','Middle but below matric/secondary F':'Middle but below matric/secondary','Graduate and above F':'Graduate and above','Matric/Secondary but below graduate F':'Matric/Secondary but below graduate'}, inplace=True)

df_males=df_males.melt(id_vars=["State Code", "Name"], var_name="literacy-group", value_name="population")
df_females=df_females.melt(id_vars=["State Code", "Name"], var_name="literacy-group", value_name="population")

language_data= pd.read_excel('DDW-C19-0000.xlsx')

language_data=language_data.loc[(language_data['Unnamed: 3'] == 'Total' ) & ((language_data['Unnamed: 4'] == 'Illiterate') | (language_data['Unnamed: 4'] == 'Literate') | (language_data['Unnamed: 4'] == 'Literate but below primary') | (language_data['Unnamed: 4'] == 'Primary but below middle') | (language_data['Unnamed: 4'] == 'Middle but below matric/secondary') | (language_data['Unnamed: 4'] == 'Matric/Secondary but below graduate') | (language_data['Unnamed: 4'] == 'Graduate and above'))]

language_data.rename(columns={'C-19 POPULATION BY BILINGUALISM, TRILINGUALISM, EDUCATIONAL LEVEL AND SEX':'State Code','Unnamed: 2':'Name','Unnamed: 4':'literacy-group','Unnamed: 6':'Second language M','Unnamed: 7':'Second language F','Unnamed: 9':'Third language M','Unnamed: 10':'Third language F'}, inplace=True)

language_data=language_data.drop(['Unnamed: 1','Unnamed: 3','Unnamed: 5','Unnamed: 8'],axis=1)

language_data=language_data.reset_index()
language_data.drop('index',axis=1,inplace=True)

language_data_males=language_data[['State Code', 'Name', 'literacy-group', 'Second language M', 'Third language M']]
language_data_females=language_data[['State Code', 'Name', 'literacy-group', 'Second language F', 'Third language F']]

result_males=pd.merge(language_data_males,df_males,on=['State Code','literacy-group'])
result_females=pd.merge(language_data_females,df_females,on=['State Code','literacy-group'])

result_males['Exactly one']=((result_males['population']-result_males['Second language M']))/result_males['population']
result_males['Exactly two']=((result_males['Second language M']-result_males['Third language M']))/result_males['population']
result_males['Three or more']=(result_males['Third language M']/result_males['population'])
result_males=result_males[['State Code','Name_x','literacy-group','Three or more','Exactly two','Exactly one']]

result_females['Exactly one']=((result_females['population']-result_females['Second language F']))/result_females['population']
result_females['Exactly two']=((result_females['Second language F']-result_females['Third language F']))/result_females['population']
result_females['Three or more']=(result_females['Third language F']/result_females['population'])
result_females=result_females[['State Code','Name_x','literacy-group','Three or more','Exactly two','Exactly one']]

# Ratio of 3

ans_a=result_males[['State Code', 'Name_x', 'literacy-group', 'Three or more']]
ans_a=ans_a.rename(columns={'literacy-group':'literacy-group-males','Three or more':'ratio-males'})
idx=ans_a.groupby(['Name_x'])['ratio-males'].transform(max)==ans_a['ratio-males']
df1=ans_a[idx]

ans_a=result_females[['State Code', 'Name_x', 'literacy-group', 'Three or more']]
ans_a=ans_a.rename(columns={'literacy-group':'literacy-group-females','Three or more':'ratio-females'})
idx=ans_a.groupby(['Name_x'])['ratio-females'].transform(max)==ans_a['ratio-females']
df2=ans_a[idx]

literacy_a=pd.merge(df1,df2,on=['State Code','Name_x'])

literacy_a=literacy_a.drop(["Name_x"],axis=1)

literacy_a.to_csv('literacy-gender-a.csv')

# Ratio of 2

ans_b=result_males[['State Code', 'Name_x', 'literacy-group', 'Exactly two']]
ans_b=ans_b.rename(columns={'literacy-group':'literacy-group-males','Exactly two':'ratio-males'})
idx=ans_b.groupby(['Name_x'])['ratio-males'].transform(max)==ans_b['ratio-males']
df3=ans_b[idx]

ans_b=result_females[['State Code', 'Name_x', 'literacy-group', 'Exactly two']]
ans_b=ans_b.rename(columns={'literacy-group':'literacy-group-females','Exactly two':'ratio-females'})
idx=ans_b.groupby(['Name_x'])['ratio-females'].transform(max)==ans_b['ratio-females']
df4=ans_b[idx]

literacy_b=pd.merge(df3,df4,on=['State Code','Name_x'])

literacy_b=literacy_b.drop(["Name_x"],axis=1)

literacy_b.to_csv('literacy-gender-b.csv')

# Ratio of 1

ans_c=result_males[['State Code', 'Name_x', 'literacy-group', 'Exactly one']]
ans_c=ans_c.rename(columns={'literacy-group':'literacy-group-males','Exactly one':'ratio-males'})
idx=ans_c.groupby(['Name_x'])['ratio-males'].transform(max)==ans_c['ratio-males']
df5=ans_c[idx]

ans_c=result_females[['State Code', 'Name_x', 'literacy-group', 'Exactly one']]
ans_c=ans_c.rename(columns={'literacy-group':'literacy-group-females','Exactly one':'ratio-females'})
idx=ans_c.groupby(['Name_x'])['ratio-females'].transform(max)==ans_c['ratio-females']
df6=ans_c[idx]

literacy_c=pd.merge(df5,df6,on=['State Code','Name_x'])

literacy_c=literacy_c.drop(["Name_x"],axis=1)

literacy_c.to_csv('literacy-gender-c.csv')
