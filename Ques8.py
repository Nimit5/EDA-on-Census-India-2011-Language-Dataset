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

# Using C-13 SINGLE YEAR AGE RETURNS BY RESIDENCE AND SEX File

df=pd.read_excel('DDW-0000C-13.xls')

df=df.dropna()

# Rename columns
df.rename(columns={'Unnamed: 1':'State Code','Unnamed: 3': 'State','C-13 SINGLE YEAR AGE RETURNS BY RESIDENCE AND SEX ':'Age','Unnamed: 5' :'Population' ,'Unnamed: 6' :'Males' ,'Unnamed: 7' :'Females'}, inplace=True)

age_data=df[["State Code","State","Age","Males","Females"]]

# Generating total population for age group 5-9

options1=[5,6,7,8,9]
df1=age_data.loc[age_data['Age'].isin(options1)]
temp1=pd.DataFrame(df1.groupby(['State Code','State']).aggregate({'Males': 'sum','Females': 'sum'}))
temp1['Age-group']="5-9"

# Generating total population for age group 10-14

options2=[10,11,12,13,14]
df2=age_data.loc[age_data['Age'].isin(options2)]
temp2=pd.DataFrame(df2.groupby(['State Code','State']).aggregate({'Males': 'sum','Females': 'sum'}))
temp2['Age-group']="10-14"

# Generating total population for age group 15-19

options3=[15,16,17,18,19]
df3=age_data.loc[age_data['Age'].isin(options3)]
temp3=pd.DataFrame(df3.groupby(['State Code','State']).aggregate({'Males': 'sum','Females': 'sum'}))
temp3['Age-group']="15-19"

# Generating total population for age group 20-24

options4=[20,21,22,23,24]
df4=age_data.loc[age_data['Age'].isin(options4)]
temp4=pd.DataFrame(df4.groupby(['State Code','State']).aggregate({'Males': 'sum','Females': 'sum'}))
temp4['Age-group']="20-24"

# Generating total population for age group 25-29

options5=[25,26,27,28,29]
df5=age_data.loc[age_data['Age'].isin(options5)]
temp5=pd.DataFrame(df5.groupby(['State Code','State']).aggregate({'Males': 'sum','Females': 'sum'}))
temp5['Age-group']="25-29"

# Generating total population for age group 30-49

options6=[30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49]
df6=age_data.loc[age_data['Age'].isin(options6)]
temp6=pd.DataFrame(df6.groupby(['State Code','State']).aggregate({'Males': 'sum','Females': 'sum'}))
temp6['Age-group']="30-49"

# Generating total population for age group 50-69

options7=[50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69]
df7=age_data.loc[age_data['Age'].isin(options7)]
temp7=pd.DataFrame(df7.groupby(['State Code','State']).aggregate({'Males': 'sum','Females': 'sum'}))
temp7['Age-group']="50-69"

# Generating total population for age group 70+

options8=[70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,"100+"]
df8=age_data.loc[age_data['Age'].isin(options8)]
temp8=pd.DataFrame(df8.groupby(['State Code','State']).aggregate({'Males': 'sum','Females': 'sum'}))
temp8['Age-group']="70+"

frames=[temp1,temp2,temp3,temp4,temp5,temp6,temp7,temp8]
age_group_data=pd.concat(frames)

result=pd.merge(language_data,age_group_data,on=["State Code","Age-group"])

result=result.drop(['Unnamed: 1', 'Total/Rural/Urban','Second Language Total','Third Language Total'], axis = 1)

result["Only One Language Males"]=result["Males"]-result["Second Language Males"]
result["Only One Language Females"]=result["Females"]-result["Second Language Females"]
result["Exactly Two Language Males"]=result["Second Language Males"]-result["Third Language Males"]
result["Exactly Two Language Females"]=result["Second Language Females"]-result["Third Language Females"]

result["Ratio of 3 Males"]=result["Third Language Males"]/result["Males"]
result["Ratio of 3 Females"]=result["Third Language Females"]/result["Females"]
result["Ratio of 2 Males"]=result["Exactly Two Language Males"]/result["Males"]
result["Ratio of 2 Females"]=result["Exactly Two Language Females"]/result["Females"]
result["Ratio of 1 Males"]=result["Only One Language Males"]/result["Males"]
result["Ratio of 1 Females"]=result["Only One Language Females"]/result["Females"]

df3_males=result[['State Code','Age-group','Ratio of 3 Males']]
df3_females=result[['State Code','Age-group','Ratio of 3 Females']]

idx=df3_males.groupby(['State Code'])['Ratio of 3 Males'].transform(max)==result['Ratio of 3 Males']
df3_males=df3_males[idx]

idx=df3_females.groupby(['State Code'])['Ratio of 3 Females'].transform(max)==result['Ratio of 3 Females']
df3_females=df3_females[idx]

df3_males=df3_males.rename(columns={'State Code':'state/ut','Age-group':'age-group-males','Ratio of 3 Males':'ratio-males'})
df3_females=df3_females.rename(columns={'State Code':'state/ut','Age-group':'age-group-females','Ratio of 3 Females':'ratio-females'})

result_a=pd.merge(df3_males,df3_females,on='state/ut')
result_a.to_csv('age-gender-a.csv',index=False)


df2_males=result[['State Code','Age-group','Ratio of 2 Males']]
df2_females=result[['State Code','Age-group','Ratio of 2 Females']]

idx=df2_males.groupby(['State Code'])['Ratio of 2 Males'].transform(max)==result['Ratio of 2 Males']
df2_males=df2_males[idx]

idx=df2_females.groupby(['State Code'])['Ratio of 2 Females'].transform(max)==result['Ratio of 2 Females']
df2_females=df2_females[idx]

df2_males=df2_males.rename(columns={'State Code':'state/ut','Age-group':'age-group-males','Ratio of 2 Males':'ratio-males'})
df2_females=df2_females.rename(columns={'State Code':'state/ut','Age-group':'age-group-females','Ratio of 2 Females':'ratio-females'})

result_b=pd.merge(df2_males,df2_females,on='state/ut')
result_b.to_csv('age-gender-b.csv',index=False)



df1_males=result[['State Code','Age-group','Ratio of 1 Males']]
df1_females=result[['State Code','Age-group','Ratio of 1 Females']]

idx=df1_males.groupby(['State Code'])['Ratio of 1 Males'].transform(max)==result['Ratio of 1 Males']
df1_males=df1_males[idx]

idx=df1_females.groupby(['State Code'])['Ratio of 1 Females'].transform(max)==result['Ratio of 1 Females']
df1_females=df1_females[idx]

df1_males=df1_males.rename(columns={'State Code':'state/ut','Age-group':'age-group-males','Ratio of 1 Males':'ratio-males'})
df1_females=df1_females.rename(columns={'State Code':'state/ut','Age-group':'age-group-females','Ratio of 1 Females':'ratio-females'})

result_c=pd.merge(df1_males,df1_females,on='state/ut')
result_c.to_csv('age-gender-c.csv',index=False)

