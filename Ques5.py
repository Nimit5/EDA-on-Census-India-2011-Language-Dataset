
# Importing libraries 

import csv
import pandas as pd
import numpy as np
import warnings 
warnings.filterwarnings('ignore')

# Using C-18 Population By Bilingualism, Trilingualism, Age And Sex File
df=pd.read_excel('DDW-C18-0000.xlsx')

# Rename columns
df.rename(columns={'C-18 POPULATION BY BILINGUALISM, TRILINGUALISM, AGE AND SEX':'State Code','Unnamed: 2':'State','Unnamed: 3': 'Total/Rural/Urban', 'Unnamed: 4' :'Age-group' ,'Unnamed: 5' :'Second Language Total' ,'Unnamed: 6' :'Second Language Males' ,'Unnamed: 7' :'Second Language Females' ,'Unnamed: 8' :'Third Language Total','Unnamed: 9' :'Third Language Males','Unnamed: 10' :'Third Language Females' }, inplace=True)

language_data=df[(df["Total/Rural/Urban"]=="Total")]

language_data=language_data[['State Code','State','Age-group','Third Language Total']]

# Using C-13 Population By Bilingualism, Trilingualism, Age And Sex File

df=pd.read_excel('DDW-0000C-13.xls')

# Rename columns
df.rename(columns={'Unnamed: 1':'State Code','Unnamed: 3': 'State','C-13 SINGLE YEAR AGE RETURNS BY RESIDENCE AND SEX ':'Age','Unnamed: 5' :'Population' ,'Unnamed: 6' :'Males' ,'Unnamed: 7' :'Females'}, inplace=True)

df=df.dropna()

age_data=df

age_data=age_data[["State Code","State","Age","Population"]]

# Generating total population for age group 5-9

options1=[5,6,7,8,9]
df1=age_data.loc[age_data['Age'].isin(options1)]
temp1=pd.DataFrame(df1.groupby(['State Code','State'])['Population'].agg('sum'))
temp1['Age-group']="5-9"

# Generating total population for age group 10-14

options2=[10,11,12,13,14]
df2=age_data.loc[age_data['Age'].isin(options2)]
temp2=pd.DataFrame(df2.groupby(['State Code','State'])['Population'].agg('sum'))
temp2['Age-group']="10-14"

# Generating total population for age group 15-19

options3=[15,16,17,18,19]
df3=age_data.loc[age_data['Age'].isin(options3)]
temp3=pd.DataFrame(df3.groupby(['State Code','State'])['Population'].agg('sum'))
temp3['Age-group']="15-19"

# Generating total population for age group 20-24

options4=[20,21,22,23,24]
df4=age_data.loc[age_data['Age'].isin(options4)]
temp4=pd.DataFrame(df4.groupby(['State Code','State'])['Population'].agg('sum'))
temp4['Age-group']="20-24"

# Generating total population for age group 25-29

options5=[25,26,27,28,29]
df5=age_data.loc[age_data['Age'].isin(options5)]
temp5=pd.DataFrame(df5.groupby(['State Code','State'])['Population'].agg('sum'))
temp5['Age-group']="25-29"

# Generating total population for age group 30-49

options6=[30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49]
df6=age_data.loc[age_data['Age'].isin(options6)]
temp6=pd.DataFrame(df6.groupby(['State Code','State'])['Population'].agg('sum'))
temp6['Age-group']="30-49"

# Generating total population for age group 50-69

options7=[50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69]
df7=age_data.loc[age_data['Age'].isin(options7)]
temp7=pd.DataFrame(df7.groupby(['State Code','State'])['Population'].agg('sum'))
temp7['Age-group']="50-69"

# Generating total population for age group 70+

options8=[70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,"100+"]
df8=age_data.loc[age_data['Age'].isin(options8)]
temp8=pd.DataFrame(df8.groupby(['State Code','State'])['Population'].agg('sum'))
temp8['Age-group']="70+"

frames=[temp1,temp2,temp3,temp4,temp5,temp6,temp7,temp8]
age_group_data=pd.concat(frames)

result=pd.merge(language_data,age_group_data,on=["State Code","Age-group"])

result["Percentage"]=result["Third Language Total"]/result["Population"]

result["Percentage"]=result["Percentage"]*100

idx=result.groupby(['State Code','State'])['Percentage'].transform(max)==result['Percentage']

answer=result[idx]

answer=answer[["State Code","Age-group","Percentage"]]

answer=answer.rename(columns={'State Code':'state/ut'})

answer.reset_index(drop=True, inplace=True)

answer.to_csv("age-india.csv")

