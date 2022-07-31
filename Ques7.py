# Importing libraries 

import csv
import pandas as pd
import numpy as np
import warnings 
warnings.filterwarnings('ignore')

# Part a

# List to store final answers for part a

region_wise_ans=[]

# Function to find top three most spoken languages in Central Region 
def Central_Region():

    UP_data=pd.read_excel('DDW-C17-0900.XLSX')
    CG_data=pd.read_excel('DDW-C17-2200.XLSX')
    MP_data=pd.read_excel('DDW-C17-2300.XLSX')

    UP_data.rename(columns={'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM':'State Code','Unnamed: 1':'State','Unnamed: 2':'Lang Code','Unnamed: 3': 'Lang', 'Unnamed: 4' :'Total' ,'Unnamed: 5' :'Males' ,'Unnamed: 6' :'Females' }, inplace=True)
    CG_data.rename(columns={'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM':'State Code','Unnamed: 1':'State','Unnamed: 2':'Lang Code','Unnamed: 3': 'Lang', 'Unnamed: 4' :'Total' ,'Unnamed: 5' :'Males' ,'Unnamed: 6' :'Females' }, inplace=True)
    MP_data.rename(columns={'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM':'State Code','Unnamed: 1':'State','Unnamed: 2':'Lang Code','Unnamed: 3': 'Lang', 'Unnamed: 4' :'Total' ,'Unnamed: 5' :'Males' ,'Unnamed: 6' :'Females' }, inplace=True)

    UP_data=UP_data[["State","Lang Code","Lang","Total","Males","Females"]]
    CG_data=CG_data[["State","Lang Code","Lang","Total","Males","Females"]]
    MP_data=MP_data[["State","Lang Code","Lang","Total","Males","Females"]]

    UP_data=UP_data.dropna()
    CG_data=CG_data.dropna()
    MP_data=MP_data.dropna()

    UP_data=UP_data[1:-1]
    CG_data=CG_data[1:-1]
    MP_data=MP_data[1:-1]

    Central_data=pd.concat([UP_data,CG_data,MP_data])
    Central_data=Central_data.drop(["State","Males","Females","Lang Code"],axis=1)
    Central_data=Central_data.groupby(Central_data['Lang'],as_index=False).aggregate({'Total':'sum',}).reindex(columns=Central_data.columns)
    Sorted_Central_data=Central_data.sort_values("Total",ascending=False)
    l=["Central"]
    for i in range(3):
        temp=Sorted_Central_data.iloc[i]["Lang"]
        l.append(temp)
    region_wise_ans.append(l)

# Function to find top three most spoken languages in East Region 
def East_Region():
    
    BH_data=pd.read_excel('DDW-C17-1000.XLSX')
    WB_data=pd.read_excel('DDW-C17-1900.XLSX')
    OR_data=pd.read_excel('DDW-C17-2100.XLSX')
    JH_data=pd.read_excel('DDW-C17-2000.XLSX')
    
    BH_data.rename(columns={'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM':'State Code','Unnamed: 1':'State','Unnamed: 2':'Lang Code','Unnamed: 3': 'Lang', 'Unnamed: 4' :'Total' ,'Unnamed: 5' :'Males' ,'Unnamed: 6' :'Females' }, inplace=True)
    WB_data.rename(columns={'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM':'State Code','Unnamed: 1':'State','Unnamed: 2':'Lang Code','Unnamed: 3': 'Lang', 'Unnamed: 4' :'Total' ,'Unnamed: 5' :'Males' ,'Unnamed: 6' :'Females' }, inplace=True)
    OR_data.rename(columns={'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM':'State Code','Unnamed: 1':'State','Unnamed: 2':'Lang Code','Unnamed: 3': 'Lang', 'Unnamed: 4' :'Total' ,'Unnamed: 5' :'Males' ,'Unnamed: 6' :'Females' }, inplace=True)
    JH_data.rename(columns={'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM':'State Code','Unnamed: 1':'State','Unnamed: 2':'Lang Code','Unnamed: 3': 'Lang', 'Unnamed: 4' :'Total' ,'Unnamed: 5' :'Males' ,'Unnamed: 6' :'Females' }, inplace=True)
    
    BH_data=BH_data[["State","Lang Code","Lang","Total","Males","Females"]]
    WB_data=WB_data[["State","Lang Code","Lang","Total","Males","Females"]]
    OR_data=OR_data[["State","Lang Code","Lang","Total","Males","Females"]]
    JH_data=JH_data[["State","Lang Code","Lang","Total","Males","Females"]]
    
    BH_data=BH_data.dropna()
    WB_data=WB_data.dropna()
    OR_data=OR_data.dropna()
    JH_data=JH_data.dropna()
    
    BH_data=BH_data[1:-1]
    WB_data=WB_data[1:-1]
    OR_data=OR_data[1:-1]
    JH_data=JH_data[1:-1]
    
    East_data=pd.concat([BH_data,WB_data,OR_data,JH_data])
    East_data=East_data.drop(["State","Males","Females","Lang Code"],axis=1)
    East_data=East_data.groupby(East_data['Lang'],as_index=False).aggregate({'Total':'sum',}).reindex(columns=East_data.columns)
    Sorted_East_data=East_data.sort_values("Total",ascending=False)
    l=["East"]
    for i in range(3):
        temp=Sorted_East_data.iloc[i]["Lang"]
        l.append(temp)
    region_wise_ans.append(l)

# Function to find top three most spoken languages in North Region 
def North_Region():
    
    JK_data=pd.read_excel('DDW-C17-0100.XLSX')
    # Ladakh_data=Not Available
    PN_data=pd.read_excel('DDW-C17-0300.XLSX')
    HP_data=pd.read_excel('DDW-C17-0200.XLSX')
    HR_data=pd.read_excel('DDW-C17-0600.XLSX')
    UK_data=pd.read_excel('DDW-C17-0500.XLSX')
    Delhi_data=pd.read_excel('DDW-C17-0700.XLSX')
    Chandigarh_data=pd.read_excel('DDW-C17-0400.XLSX')

    JK_data.rename(columns={'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM':'State Code','Unnamed: 1':'State','Unnamed: 2':'Lang Code','Unnamed: 3': 'Lang', 'Unnamed: 4' :'Total' ,'Unnamed: 5' :'Males' ,'Unnamed: 6' :'Females' }, inplace=True)
    PN_data.rename(columns={'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM':'State Code','Unnamed: 1':'State','Unnamed: 2':'Lang Code','Unnamed: 3': 'Lang', 'Unnamed: 4' :'Total' ,'Unnamed: 5' :'Males' ,'Unnamed: 6' :'Females' }, inplace=True)
    HP_data.rename(columns={'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM':'State Code','Unnamed: 1':'State','Unnamed: 2':'Lang Code','Unnamed: 3': 'Lang', 'Unnamed: 4' :'Total' ,'Unnamed: 5' :'Males' ,'Unnamed: 6' :'Females' }, inplace=True)
    HR_data.rename(columns={'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM':'State Code','Unnamed: 1':'State','Unnamed: 2':'Lang Code','Unnamed: 3': 'Lang', 'Unnamed: 4' :'Total' ,'Unnamed: 5' :'Males' ,'Unnamed: 6' :'Females' }, inplace=True)
    UK_data.rename(columns={'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM':'State Code','Unnamed: 1':'State','Unnamed: 2':'Lang Code','Unnamed: 3': 'Lang', 'Unnamed: 4' :'Total' ,'Unnamed: 5' :'Males' ,'Unnamed: 6' :'Females' }, inplace=True)
    Delhi_data.rename(columns={'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM':'State Code','Unnamed: 1':'State','Unnamed: 2':'Lang Code','Unnamed: 3': 'Lang', 'Unnamed: 4' :'Total' ,'Unnamed: 5' :'Males' ,'Unnamed: 6' :'Females' }, inplace=True)
    Chandigarh_data.rename(columns={'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM':'State Code','Unnamed: 1':'State','Unnamed: 2':'Lang Code','Unnamed: 3': 'Lang', 'Unnamed: 4' :'Total' ,'Unnamed: 5' :'Males' ,'Unnamed: 6' :'Females' }, inplace=True)

    JK_data=JK_data[["State","Lang","Total"]]
    PN_data=PN_data[["State","Lang","Total"]]
    HP_data=HP_data[["State","Lang","Total"]]
    HR_data=HR_data[["State","Lang","Total"]]
    UK_data=UK_data[["State","Lang","Total"]]
    Delhi_data=Delhi_data[["State","Lang","Total"]]
    Chandigarh_data=Chandigarh_data[["State","Lang","Total"]]
    
    JK_data=JK_data.dropna()
    PN_data=PN_data.dropna()
    HP_data=HP_data.dropna()
    HR_data=HR_data.dropna()
    UK_data=UK_data.dropna()
    Delhi_data=Delhi_data.dropna()
    Chandigarh_data=Chandigarh_data.dropna()
    
    JK_data=JK_data[1:-1]
    PN_data=PN_data[1:-1]
    HP_data=HP_data[1:-1]
    HR_data=HR_data[1:-1]
    UK_data=UK_data[1:-1]
    Delhi_data=Delhi_data[1:-1]
    Chandigarh_data=Chandigarh_data[1:-1]

    North_data=pd.concat([JK_data,PN_data,HP_data,HR_data,UK_data,Delhi_data,Chandigarh_data])
    North_data=North_data.drop(["State"],axis=1)
    North_data=North_data.groupby(North_data['Lang'],as_index=False).aggregate({'Total':'sum',}).reindex(columns=North_data.columns)
    Sorted_North_data=North_data.sort_values("Total",ascending=False)
    l=["North"]
    for i in range(3):
        temp=Sorted_North_data.iloc[i]["Lang"]
        l.append(temp)
    region_wise_ans.append(l)

# Function to find top three most spoken languages in North East Region 
def North_East_Region():
    
    AS_data=pd.read_excel('DDW-C17-1800.XLSX')
    SK_data=pd.read_excel('DDW-C17-1100.XLSX')
    MG_data=pd.read_excel('DDW-C17-1700.XLSX')
    TR_data=pd.read_excel('DDW-C17-1600.XLSX')
    AR_data=pd.read_excel('DDW-C17-1200.XLSX')
    MN_data=pd.read_excel('DDW-C17-1400.XLSX')
    NG_data=pd.read_excel('DDW-C17-1300.XLSX')
    MZ_data=pd.read_excel('DDW-C17-1500.XLSX')
    Andaman_data=pd.read_excel('DDW-C17-3500.XLSX')

    AS_data.rename(columns={'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM':'State Code','Unnamed: 1':'State','Unnamed: 2':'Lang Code','Unnamed: 3': 'Lang', 'Unnamed: 4' :'Total' ,'Unnamed: 5' :'Males' ,'Unnamed: 6' :'Females' }, inplace=True)
    SK_data.rename(columns={'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM':'State Code','Unnamed: 1':'State','Unnamed: 2':'Lang Code','Unnamed: 3': 'Lang', 'Unnamed: 4' :'Total' ,'Unnamed: 5' :'Males' ,'Unnamed: 6' :'Females' }, inplace=True)
    MG_data.rename(columns={'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM':'State Code','Unnamed: 1':'State','Unnamed: 2':'Lang Code','Unnamed: 3': 'Lang', 'Unnamed: 4' :'Total' ,'Unnamed: 5' :'Males' ,'Unnamed: 6' :'Females' }, inplace=True)
    TR_data.rename(columns={'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM':'State Code','Unnamed: 1':'State','Unnamed: 2':'Lang Code','Unnamed: 3': 'Lang', 'Unnamed: 4' :'Total' ,'Unnamed: 5' :'Males' ,'Unnamed: 6' :'Females' }, inplace=True)
    AR_data.rename(columns={'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM':'State Code','Unnamed: 1':'State','Unnamed: 2':'Lang Code','Unnamed: 3': 'Lang', 'Unnamed: 4' :'Total' ,'Unnamed: 5' :'Males' ,'Unnamed: 6' :'Females' }, inplace=True)
    MN_data.rename(columns={'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM':'State Code','Unnamed: 1':'State','Unnamed: 2':'Lang Code','Unnamed: 3': 'Lang', 'Unnamed: 4' :'Total' ,'Unnamed: 5' :'Males' ,'Unnamed: 6' :'Females' }, inplace=True)
    NG_data.rename(columns={'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM':'State Code','Unnamed: 1':'State','Unnamed: 2':'Lang Code','Unnamed: 3': 'Lang', 'Unnamed: 4' :'Total' ,'Unnamed: 5' :'Males' ,'Unnamed: 6' :'Females' }, inplace=True)
    MZ_data.rename(columns={'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM':'State Code','Unnamed: 1':'State','Unnamed: 2':'Lang Code','Unnamed: 3': 'Lang', 'Unnamed: 4' :'Total' ,'Unnamed: 5' :'Males' ,'Unnamed: 6' :'Females' }, inplace=True)
    Andaman_data.rename(columns={'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM':'State Code','Unnamed: 1':'State','Unnamed: 2':'Lang Code','Unnamed: 3': 'Lang', 'Unnamed: 4' :'Total' ,'Unnamed: 5' :'Males' ,'Unnamed: 6' :'Females' }, inplace=True)

    AS_data=AS_data[["State","Lang Code","Lang","Total","Males","Females"]]
    SK_data=SK_data[["State","Lang Code","Lang","Total","Males","Females"]]
    MG_data=MG_data[["State","Lang Code","Lang","Total","Males","Females"]]
    TR_data=TR_data[["State","Lang Code","Lang","Total","Males","Females"]]
    AR_data=AR_data[["State","Lang Code","Lang","Total","Males","Females"]]
    MN_data=MN_data[["State","Lang Code","Lang","Total","Males","Females"]]
    NG_data=NG_data[["State","Lang Code","Lang","Total","Males","Females"]]
    MZ_data=MZ_data[["State","Lang Code","Lang","Total","Males","Females"]]
    Andaman_data=Andaman_data[["State","Lang Code","Lang","Total","Males","Females"]]

    AS_data=AS_data.dropna()
    SK_data=SK_data.dropna()
    MG_data=MG_data.dropna()
    TR_data=TR_data.dropna()
    AR_data=AR_data.dropna()
    MN_data=MN_data.dropna()
    NG_data=NG_data.dropna()
    MZ_data=MZ_data.dropna()
    Andaman_data=Andaman_data.dropna()

    AS_data=AS_data[1:-1]
    SK_data=SK_data[1:-1]
    MG_data=MG_data[1:-1]
    TR_data=TR_data[1:-1]
    AR_data=AR_data[1:-1]
    MN_data=MN_data[1:-1]
    NG_data=NG_data[1:-1]
    MZ_data=MZ_data[1:-1]
    Andaman_data=Andaman_data[1:-1]

    North_East_data=pd.concat([AS_data,SK_data,MG_data,TR_data,AR_data,MN_data,NG_data,MZ_data,Andaman_data])
    North_East_data=North_East_data.drop(["State","Males","Females","Lang Code"],axis=1)
    North_East_data=North_East_data.groupby(North_East_data['Lang'],as_index=False).aggregate({'Total':'sum',}).reindex(columns=North_East_data.columns)
    Sorted_North_East_data=North_East_data.sort_values("Total",ascending=False)
    l=["North-East"]
    for i in range(3):
        temp=Sorted_North_East_data.iloc[i]["Lang"]
        l.append(temp)
    region_wise_ans.append(l)

# Function to find top three most spoken languages in South Region 
def South_Region():
    
    KT_data=pd.read_excel('DDW-C17-2900.XLSX')
    # TG = data not available
    AP_data=pd.read_excel('DDW-C17-2800.XLSX')
    TN_data=pd.read_excel('DDW-C17-3300.XLSX')
    KL_data=pd.read_excel('DDW-C17-3200.XLSX')
    Lakshadweep_data=pd.read_excel('DDW-C17-3100.XLSX')
    Puducherry_data=pd.read_excel('DDW-C17-3400.XLSX')

    KT_data.rename(columns={'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM':'State Code','Unnamed: 1':'State','Unnamed: 2':'Lang Code','Unnamed: 3': 'Lang', 'Unnamed: 4' :'Total' ,'Unnamed: 5' :'Males' ,'Unnamed: 6' :'Females' }, inplace=True)
    AP_data.rename(columns={'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM':'State Code','Unnamed: 1':'State','Unnamed: 2':'Lang Code','Unnamed: 3': 'Lang', 'Unnamed: 4' :'Total' ,'Unnamed: 5' :'Males' ,'Unnamed: 6' :'Females' }, inplace=True)
    TN_data.rename(columns={'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM':'State Code','Unnamed: 1':'State','Unnamed: 2':'Lang Code','Unnamed: 3': 'Lang', 'Unnamed: 4' :'Total' ,'Unnamed: 5' :'Males' ,'Unnamed: 6' :'Females' }, inplace=True)
    KL_data.rename(columns={'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM':'State Code','Unnamed: 1':'State','Unnamed: 2':'Lang Code','Unnamed: 3': 'Lang', 'Unnamed: 4' :'Total' ,'Unnamed: 5' :'Males' ,'Unnamed: 6' :'Females' }, inplace=True)
    Lakshadweep_data.rename(columns={'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM':'State Code','Unnamed: 1':'State','Unnamed: 2':'Lang Code','Unnamed: 3': 'Lang', 'Unnamed: 4' :'Total' ,'Unnamed: 5' :'Males' ,'Unnamed: 6' :'Females' }, inplace=True)
    Puducherry_data.rename(columns={'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM':'State Code','Unnamed: 1':'State','Unnamed: 2':'Lang Code','Unnamed: 3': 'Lang', 'Unnamed: 4' :'Total' ,'Unnamed: 5' :'Males' ,'Unnamed: 6' :'Females' }, inplace=True)

    KT_data=KT_data[["State","Lang Code","Lang","Total","Males","Females"]]
    AP_data=AP_data[["State","Lang Code","Lang","Total","Males","Females"]]
    TN_data=TN_data[["State","Lang Code","Lang","Total","Males","Females"]]
    KL_data=KL_data[["State","Lang Code","Lang","Total","Males","Females"]]
    Lakshadweep_data=Lakshadweep_data[["State","Lang Code","Lang","Total","Males","Females"]]
    Puducherry_data=Puducherry_data[["State","Lang Code","Lang","Total","Males","Females"]]

    KT_data=KT_data.dropna()
    AP_data=AP_data.dropna()
    TN_data=TN_data.dropna()
    KL_data=KL_data.dropna()
    Lakshadweep_data=Lakshadweep_data.dropna()
    Puducherry_data=Puducherry_data.dropna()

    KT_data=KT_data[1:-1]
    AP_data=AP_data[1:-1]
    TN_data=TN_data[1:-1]
    KL_data=KL_data[1:-1]
    Lakshadweep_data=Lakshadweep_data[1:-1]
    Puducherry_data=Puducherry_data[1:-1]

    South_data=pd.concat([KT_data,AP_data,TN_data,KL_data,Lakshadweep_data,Puducherry_data])
    South_data=South_data.drop(["State","Males","Females","Lang Code"],axis=1)
    South_data=South_data.groupby(South_data['Lang'],as_index=False).aggregate({'Total':'sum',}).reindex(columns=South_data.columns)
    Sorted_South_data=South_data.sort_values("Total",ascending=False)
    l=["South"]
    for i in range(3):
        temp=Sorted_South_data.iloc[i]["Lang"]
        l.append(temp)
    region_wise_ans.append(l)

# Function to find top three most spoken languages in West Region 
def West_Region():
    
    RJ_data=pd.read_excel('DDW-C17-0800.XLSX')
    GJ_data=pd.read_excel('DDW-C17-2400.XLSX')
    MH_data=pd.read_excel('DDW-C17-2700.XLSX')
    Goa_data=pd.read_excel('DDW-C17-3000.XLSX')
    Dadra_Nagar_data=pd.read_excel('DDW-C17-2600.XLSX')
    Daman_Diu_data=pd.read_excel('DDW-C17-2500.XLSX')

    RJ_data.rename(columns={'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM':'State Code','Unnamed: 1':'State','Unnamed: 2':'Lang Code','Unnamed: 3': 'Lang', 'Unnamed: 4' :'Total' ,'Unnamed: 5' :'Males' ,'Unnamed: 6' :'Females' }, inplace=True)
    GJ_data.rename(columns={'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM':'State Code','Unnamed: 1':'State','Unnamed: 2':'Lang Code','Unnamed: 3': 'Lang', 'Unnamed: 4' :'Total' ,'Unnamed: 5' :'Males' ,'Unnamed: 6' :'Females' }, inplace=True)
    MH_data.rename(columns={'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM':'State Code','Unnamed: 1':'State','Unnamed: 2':'Lang Code','Unnamed: 3': 'Lang', 'Unnamed: 4' :'Total' ,'Unnamed: 5' :'Males' ,'Unnamed: 6' :'Females' }, inplace=True)
    Goa_data.rename(columns={'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM':'State Code','Unnamed: 1':'State','Unnamed: 2':'Lang Code','Unnamed: 3': 'Lang', 'Unnamed: 4' :'Total' ,'Unnamed: 5' :'Males' ,'Unnamed: 6' :'Females' }, inplace=True)
    Dadra_Nagar_data.rename(columns={'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM':'State Code','Unnamed: 1':'State','Unnamed: 2':'Lang Code','Unnamed: 3': 'Lang', 'Unnamed: 4' :'Total' ,'Unnamed: 5' :'Males' ,'Unnamed: 6' :'Females' }, inplace=True)
    Daman_Diu_data.rename(columns={'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM':'State Code','Unnamed: 1':'State','Unnamed: 2':'Lang Code','Unnamed: 3': 'Lang', 'Unnamed: 4' :'Total' ,'Unnamed: 5' :'Males' ,'Unnamed: 6' :'Females' }, inplace=True)
    
    RJ_data=RJ_data[["State","Lang Code","Lang","Total","Males","Females"]]
    GJ_data=GJ_data[["State","Lang Code","Lang","Total","Males","Females"]]
    MH_data=MH_data[["State","Lang Code","Lang","Total","Males","Females"]]
    Goa_data=Goa_data[["State","Lang Code","Lang","Total","Males","Females"]]
    Dadra_Nagar_data=Dadra_Nagar_data[["State","Lang Code","Lang","Total","Males","Females"]]
    Daman_Diu_data=Daman_Diu_data[["State","Lang Code","Lang","Total","Males","Females"]]

    RJ_data=RJ_data.dropna()
    GJ_data=GJ_data.dropna()
    MH_data=MH_data.dropna()
    Goa_data=Goa_data.dropna()
    Dadra_Nagar_data=Dadra_Nagar_data.dropna()
    Daman_Diu_data=Daman_Diu_data.dropna()

    RJ_data=RJ_data[1:-1]
    GJ_data=GJ_data[1:-1]
    MH_data=MH_data[1:-1]
    Goa_data=Goa_data[1:-1]
    Dadra_Nagar_data=Dadra_Nagar_data[1:-1]
    Daman_Diu_data=Daman_Diu_data[1:-1]

    West_data=pd.concat([RJ_data,GJ_data,MH_data,Goa_data,Dadra_Nagar_data,Daman_Diu_data])
    West_data=West_data.drop(["State","Males","Females","Lang Code"],axis=1)
    West_data=West_data.groupby(West_data['Lang'],as_index=False).aggregate({'Total':'sum',}).reindex(columns=West_data.columns)
    Sorted_West_data=West_data.sort_values("Total",ascending=False)
    l=["West"]
    for i in range(3):
        temp=Sorted_West_data.iloc[i]["Lang"]
        l.append(temp)
    region_wise_ans.append(l)

# Executing above functions to generate outputs

Central_Region()
East_Region()
North_Region()
North_East_Region()
South_Region()
West_Region()

# Writing final results in csv 

with open('region-india-a.csv','w') as out:
    csv_out=csv.writer(out)
    csv_out.writerow(['region', 'language-1', 'language-2', 'language-3'])
    for row in region_wise_ans:
        csv_out.writerow(row)

# Part b

# List to store final answers for part b

region=[]

# Function to find top three most spoken languages in Central Region 
def Central_Region_Part_b():

    UP_data=pd.read_excel('DDW-C17-0900.XLSX')
    CG_data=pd.read_excel('DDW-C17-2200.XLSX')
    MP_data=pd.read_excel('DDW-C17-2300.XLSX')

    UP_data.rename(columns={'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM':'State Code','Unnamed: 1':'State','Unnamed: 2':'Lang Code','Unnamed: 3': 'Lang', 'Unnamed: 4' :'Total' ,'Unnamed: 5' :'Males' ,'Unnamed: 6' :'Females','Unnamed: 8' :'2nd language','Unnamed: 9' :'2nd language Total','Unnamed: 13' :'3rd language','Unnamed: 14' :'3rd language Total' }, inplace=True)
    CG_data.rename(columns={'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM':'State Code','Unnamed: 1':'State','Unnamed: 2':'Lang Code','Unnamed: 3': 'Lang', 'Unnamed: 4' :'Total' ,'Unnamed: 5' :'Males' ,'Unnamed: 6' :'Females','Unnamed: 8' :'2nd language','Unnamed: 9' :'2nd language Total','Unnamed: 13' :'3rd language','Unnamed: 14' :'3rd language Total' }, inplace=True)
    MP_data.rename(columns={'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM':'State Code','Unnamed: 1':'State','Unnamed: 2':'Lang Code','Unnamed: 3': 'Lang', 'Unnamed: 4' :'Total' ,'Unnamed: 5' :'Males' ,'Unnamed: 6' :'Females','Unnamed: 8' :'2nd language','Unnamed: 9' :'2nd language Total','Unnamed: 13' :'3rd language','Unnamed: 14' :'3rd language Total' }, inplace=True)

    df1=UP_data[["State","Lang","Total"]]
    df2=UP_data[["State","2nd language","2nd language Total"]]
    df3=UP_data[["State","3rd language","3rd language Total"]]

    df4=CG_data[["State","Lang","Total"]]
    df5=CG_data[["State","2nd language","2nd language Total"]]
    df6=CG_data[["State","3rd language","3rd language Total"]]

    df7=MP_data[["State","Lang","Total"]]
    df8=MP_data[["State","2nd language","2nd language Total"]]
    df9=MP_data[["State","3rd language","3rd language Total"]]


    df1=df1.dropna()
    df2=df2.dropna()
    df3=df3.dropna()

    df4=df4.dropna()
    df5=df5.dropna()
    df6=df6.dropna()

    df7=df7.dropna()
    df8=df8.dropna()
    df9=df9.dropna()

    df2.rename(columns={'2nd language':'Lang','2nd language Total':'Total'}, inplace=True)
    df3.rename(columns={'3rd language':'Lang','3rd language Total':'Total'}, inplace=True)

    df5.rename(columns={'2nd language':'Lang','2nd language Total':'Total'}, inplace=True)
    df6.rename(columns={'3rd language':'Lang','3rd language Total':'Total'}, inplace=True)

    df8.rename(columns={'2nd language':'Lang','2nd language Total':'Total'}, inplace=True)
    df9.rename(columns={'3rd language':'Lang','3rd language Total':'Total'}, inplace=True)

    Central_data=pd.concat([df1,df2,df3,df4,df5,df6,df7,df8,df9])

    Central_data=Central_data.drop(["State"],axis=1)
    Central_data=Central_data.groupby(Central_data['Lang'],as_index=False).aggregate({'Total':'sum',}).reindex(columns=Central_data.columns)

    Central_data=Central_data[3:] 
    
    
    Sorted_Central_data=Central_data.sort_values("Total",ascending=False)
    l=["Central"]
    for i in range(3):
        temp=Sorted_Central_data.iloc[i]["Lang"]
        l.append(temp)
    region.append(l)

# Function to find top three most spoken languages in East Region 

def East_Region_Part_b():
    
    BH_data=pd.read_excel('DDW-C17-1000.XLSX')
    WB_data=pd.read_excel('DDW-C17-1900.XLSX')
    OR_data=pd.read_excel('DDW-C17-2100.XLSX')
    JH_data=pd.read_excel('DDW-C17-2000.XLSX')
    
    BH_data.rename(columns={'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM':'State Code','Unnamed: 1':'State','Unnamed: 2':'Lang Code','Unnamed: 3': 'Lang', 'Unnamed: 4' :'Total' ,'Unnamed: 5' :'Males' ,'Unnamed: 6' :'Females','Unnamed: 8' :'2nd language','Unnamed: 9' :'2nd language Total','Unnamed: 13' :'3rd language','Unnamed: 14' :'3rd language Total' }, inplace=True)
    WB_data.rename(columns={'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM':'State Code','Unnamed: 1':'State','Unnamed: 2':'Lang Code','Unnamed: 3': 'Lang', 'Unnamed: 4' :'Total' ,'Unnamed: 5' :'Males' ,'Unnamed: 6' :'Females','Unnamed: 8' :'2nd language','Unnamed: 9' :'2nd language Total','Unnamed: 13' :'3rd language','Unnamed: 14' :'3rd language Total' }, inplace=True)
    OR_data.rename(columns={'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM':'State Code','Unnamed: 1':'State','Unnamed: 2':'Lang Code','Unnamed: 3': 'Lang', 'Unnamed: 4' :'Total' ,'Unnamed: 5' :'Males' ,'Unnamed: 6' :'Females','Unnamed: 8' :'2nd language','Unnamed: 9' :'2nd language Total','Unnamed: 13' :'3rd language','Unnamed: 14' :'3rd language Total' }, inplace=True)
    JH_data.rename(columns={'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM':'State Code','Unnamed: 1':'State','Unnamed: 2':'Lang Code','Unnamed: 3': 'Lang', 'Unnamed: 4' :'Total' ,'Unnamed: 5' :'Males' ,'Unnamed: 6' :'Females','Unnamed: 8' :'2nd language','Unnamed: 9' :'2nd language Total','Unnamed: 13' :'3rd language','Unnamed: 14' :'3rd language Total' }, inplace=True)
    
    df1=BH_data[["State","Lang","Total"]]
    df2=BH_data[["State","2nd language","2nd language Total"]]
    df3=BH_data[["State","3rd language","3rd language Total"]]

    df4=WB_data[["State","Lang","Total"]]
    df5=WB_data[["State","2nd language","2nd language Total"]]
    df6=WB_data[["State","3rd language","3rd language Total"]]

    df7=OR_data[["State","Lang","Total"]]
    df8=OR_data[["State","2nd language","2nd language Total"]]
    df9=OR_data[["State","3rd language","3rd language Total"]]

    df10=JH_data[["State","Lang","Total"]]
    df11=JH_data[["State","2nd language","2nd language Total"]]
    df12=JH_data[["State","3rd language","3rd language Total"]]

    df1=df1.dropna()
    df2=df2.dropna()
    df3=df3.dropna()

    df4=df4.dropna()
    df5=df5.dropna()
    df6=df6.dropna()

    df7=df7.dropna()
    df8=df8.dropna()
    df9=df9.dropna()

    df10=df10.dropna()
    df11=df11.dropna()
    df12=df12.dropna()

    df2.rename(columns={'2nd language':'Lang','2nd language Total':'Total'}, inplace=True)
    df3.rename(columns={'3rd language':'Lang','3rd language Total':'Total'}, inplace=True)

    df5.rename(columns={'2nd language':'Lang','2nd language Total':'Total'}, inplace=True)
    df6.rename(columns={'3rd language':'Lang','3rd language Total':'Total'}, inplace=True)

    df8.rename(columns={'2nd language':'Lang','2nd language Total':'Total'}, inplace=True)
    df9.rename(columns={'3rd language':'Lang','3rd language Total':'Total'}, inplace=True)

    df11.rename(columns={'2nd language':'Lang','2nd language Total':'Total'}, inplace=True)
    df12.rename(columns={'3rd language':'Lang','3rd language Total':'Total'}, inplace=True)
           
    East_data=pd.concat([df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12])
    East_data=East_data.drop(["State"],axis=1)
    East_data=East_data.groupby(East_data['Lang'],as_index=False).aggregate({'Total':'sum',}).reindex(columns=East_data.columns)
    
    East_data=East_data[3:]
    
    Sorted_East_data=East_data.sort_values("Total",ascending=False)
    l=["East"]
    for i in range(3):
        temp=Sorted_East_data.iloc[i]["Lang"]
        l.append(temp)
    region.append(l)

# Function to find top three most spoken languages in North Region 

def North_Region_Part_b(): 
    JK_data=pd.read_excel('DDW-C17-0100.XLSX')
    # Ladakh_data=Not Available
    PN_data=pd.read_excel('DDW-C17-0300.XLSX')
    HP_data=pd.read_excel('DDW-C17-0200.XLSX')
    HR_data=pd.read_excel('DDW-C17-0600.XLSX')
    UK_data=pd.read_excel('DDW-C17-0500.XLSX')
    Delhi_data=pd.read_excel('DDW-C17-0700.XLSX')
    Chandigarh_data=pd.read_excel('DDW-C17-0400.XLSX')
    
    JK_data.rename(columns={'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM':'State Code','Unnamed: 1':'State','Unnamed: 2':'Lang Code','Unnamed: 3': 'Lang', 'Unnamed: 4' :'Total' ,'Unnamed: 5' :'Males' ,'Unnamed: 6' :'Females','Unnamed: 8' :'2nd language','Unnamed: 9' :'2nd language Total','Unnamed: 13' :'3rd language','Unnamed: 14' :'3rd language Total' }, inplace=True)
    PN_data.rename(columns={'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM':'State Code','Unnamed: 1':'State','Unnamed: 2':'Lang Code','Unnamed: 3': 'Lang', 'Unnamed: 4' :'Total' ,'Unnamed: 5' :'Males' ,'Unnamed: 6' :'Females','Unnamed: 8' :'2nd language','Unnamed: 9' :'2nd language Total','Unnamed: 13' :'3rd language','Unnamed: 14' :'3rd language Total' }, inplace=True)
    HP_data.rename(columns={'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM':'State Code','Unnamed: 1':'State','Unnamed: 2':'Lang Code','Unnamed: 3': 'Lang', 'Unnamed: 4' :'Total' ,'Unnamed: 5' :'Males' ,'Unnamed: 6' :'Females','Unnamed: 8' :'2nd language','Unnamed: 9' :'2nd language Total','Unnamed: 13' :'3rd language','Unnamed: 14' :'3rd language Total' }, inplace=True)
    HR_data.rename(columns={'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM':'State Code','Unnamed: 1':'State','Unnamed: 2':'Lang Code','Unnamed: 3': 'Lang', 'Unnamed: 4' :'Total' ,'Unnamed: 5' :'Males' ,'Unnamed: 6' :'Females','Unnamed: 8' :'2nd language','Unnamed: 9' :'2nd language Total','Unnamed: 13' :'3rd language','Unnamed: 14' :'3rd language Total' }, inplace=True)
    UK_data.rename(columns={'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM':'State Code','Unnamed: 1':'State','Unnamed: 2':'Lang Code','Unnamed: 3': 'Lang', 'Unnamed: 4' :'Total' ,'Unnamed: 5' :'Males' ,'Unnamed: 6' :'Females','Unnamed: 8' :'2nd language','Unnamed: 9' :'2nd language Total','Unnamed: 13' :'3rd language','Unnamed: 14' :'3rd language Total' }, inplace=True)
    Delhi_data.rename(columns={'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM':'State Code','Unnamed: 1':'State','Unnamed: 2':'Lang Code','Unnamed: 3': 'Lang', 'Unnamed: 4' :'Total' ,'Unnamed: 5' :'Males' ,'Unnamed: 6' :'Females','Unnamed: 8' :'2nd language','Unnamed: 9' :'2nd language Total','Unnamed: 13' :'3rd language','Unnamed: 14' :'3rd language Total' }, inplace=True)
    Chandigarh_data.rename(columns={'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM':'State Code','Unnamed: 1':'State','Unnamed: 2':'Lang Code','Unnamed: 3': 'Lang', 'Unnamed: 4' :'Total' ,'Unnamed: 5' :'Males' ,'Unnamed: 6' :'Females','Unnamed: 8' :'2nd language','Unnamed: 9' :'2nd language Total','Unnamed: 13' :'3rd language','Unnamed: 14' :'3rd language Total' }, inplace=True)

    df1=JK_data[["State","Lang","Total"]]
    df2=JK_data[["State","2nd language","2nd language Total"]]
    df3=JK_data[["State","3rd language","3rd language Total"]]

    df4=PN_data[["State","Lang","Total"]]
    df5=PN_data[["State","2nd language","2nd language Total"]]
    df6=PN_data[["State","3rd language","3rd language Total"]]

    df7=HP_data[["State","Lang","Total"]]
    df8=HP_data[["State","2nd language","2nd language Total"]]
    df9=HP_data[["State","3rd language","3rd language Total"]]

    df10=HR_data[["State","Lang","Total"]]
    df11=HR_data[["State","2nd language","2nd language Total"]]
    df12=HR_data[["State","3rd language","3rd language Total"]]

    df13=UK_data[["State","Lang","Total"]]
    df14=UK_data[["State","2nd language","2nd language Total"]]
    df15=UK_data[["State","3rd language","3rd language Total"]]

    df16=Delhi_data[["State","Lang","Total"]]
    df17=Delhi_data[["State","2nd language","2nd language Total"]]
    df18=Delhi_data[["State","3rd language","3rd language Total"]]

    df19=Chandigarh_data[["State","Lang","Total"]]
    df20=Chandigarh_data[["State","2nd language","2nd language Total"]]
    df21=Chandigarh_data[["State","3rd language","3rd language Total"]]

    df1=df1.dropna()
    df2=df2.dropna()
    df3=df3.dropna()

    df4=df4.dropna()
    df5=df5.dropna()
    df6=df6.dropna()

    df7=df7.dropna()
    df8=df8.dropna()
    df9=df9.dropna()

    df10=df10.dropna()
    df11=df11.dropna()
    df12=df12.dropna()

    df13=df13.dropna()
    df14=df14.dropna()
    df15=df15.dropna()

    df16=df16.dropna()
    df17=df17.dropna()
    df18=df18.dropna()

    df19=df19.dropna()
    df20=df20.dropna()
    df21=df21.dropna()

    df2.rename(columns={'2nd language':'Lang','2nd language Total':'Total'}, inplace=True)
    df3.rename(columns={'3rd language':'Lang','3rd language Total':'Total'}, inplace=True)

    df5.rename(columns={'2nd language':'Lang','2nd language Total':'Total'}, inplace=True)
    df6.rename(columns={'3rd language':'Lang','3rd language Total':'Total'}, inplace=True)

    df8.rename(columns={'2nd language':'Lang','2nd language Total':'Total'}, inplace=True)
    df9.rename(columns={'3rd language':'Lang','3rd language Total':'Total'}, inplace=True)

    df11.rename(columns={'2nd language':'Lang','2nd language Total':'Total'}, inplace=True)
    df12.rename(columns={'3rd language':'Lang','3rd language Total':'Total'}, inplace=True)

    df14.rename(columns={'2nd language':'Lang','2nd language Total':'Total'}, inplace=True)
    df15.rename(columns={'3rd language':'Lang','3rd language Total':'Total'}, inplace=True)

    df17.rename(columns={'2nd language':'Lang','2nd language Total':'Total'}, inplace=True)
    df18.rename(columns={'3rd language':'Lang','3rd language Total':'Total'}, inplace=True)

    df20.rename(columns={'2nd language':'Lang','2nd language Total':'Total'}, inplace=True)
    df21.rename(columns={'3rd language':'Lang','3rd language Total':'Total'}, inplace=True)    

    North_data=pd.concat([df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12,df13,df14,df15,df16,df17,df18,df19,df20,df21])

    North_data=North_data.drop(["State"],axis=1)
    
    North_data=North_data.groupby(North_data['Lang'],as_index=False).aggregate({'Total':'sum',}).reindex(columns=North_data.columns)
    
    North_data=North_data[3:]

    Sorted_North_data=North_data.sort_values("Total",ascending=False)

    l=["North"]
    for i in range(3):
        temp=Sorted_North_data.iloc[i]["Lang"]
        l.append(temp)
    region.append(l)

# Function to find top three most spoken languages in North East Region 

def North_East_Region_Part_b():
    
    AS_data=pd.read_excel('DDW-C17-1800.XLSX')
    SK_data=pd.read_excel('DDW-C17-1100.XLSX')
    MG_data=pd.read_excel('DDW-C17-1700.XLSX')
    TR_data=pd.read_excel('DDW-C17-1600.XLSX')
    AR_data=pd.read_excel('DDW-C17-1200.XLSX')
    MN_data=pd.read_excel('DDW-C17-1400.XLSX')
    NG_data=pd.read_excel('DDW-C17-1300.XLSX')
    MZ_data=pd.read_excel('DDW-C17-1500.XLSX')
    Andaman_data=pd.read_excel('DDW-C17-3500.XLSX')

    AS_data.rename(columns={'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM':'State Code','Unnamed: 1':'State','Unnamed: 2':'Lang Code','Unnamed: 3': 'Lang', 'Unnamed: 4' :'Total' ,'Unnamed: 5' :'Males' ,'Unnamed: 6' :'Females','Unnamed: 8' :'2nd language','Unnamed: 9' :'2nd language Total','Unnamed: 13' :'3rd language','Unnamed: 14' :'3rd language Total' }, inplace=True)
    SK_data.rename(columns={'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM':'State Code','Unnamed: 1':'State','Unnamed: 2':'Lang Code','Unnamed: 3': 'Lang', 'Unnamed: 4' :'Total' ,'Unnamed: 5' :'Males' ,'Unnamed: 6' :'Females','Unnamed: 8' :'2nd language','Unnamed: 9' :'2nd language Total','Unnamed: 13' :'3rd language','Unnamed: 14' :'3rd language Total' }, inplace=True)
    MG_data.rename(columns={'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM':'State Code','Unnamed: 1':'State','Unnamed: 2':'Lang Code','Unnamed: 3': 'Lang', 'Unnamed: 4' :'Total' ,'Unnamed: 5' :'Males' ,'Unnamed: 6' :'Females','Unnamed: 8' :'2nd language','Unnamed: 9' :'2nd language Total','Unnamed: 13' :'3rd language','Unnamed: 14' :'3rd language Total' }, inplace=True)
    TR_data.rename(columns={'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM':'State Code','Unnamed: 1':'State','Unnamed: 2':'Lang Code','Unnamed: 3': 'Lang', 'Unnamed: 4' :'Total' ,'Unnamed: 5' :'Males' ,'Unnamed: 6' :'Females','Unnamed: 8' :'2nd language','Unnamed: 9' :'2nd language Total','Unnamed: 13' :'3rd language','Unnamed: 14' :'3rd language Total' }, inplace=True)
    AR_data.rename(columns={'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM':'State Code','Unnamed: 1':'State','Unnamed: 2':'Lang Code','Unnamed: 3': 'Lang', 'Unnamed: 4' :'Total' ,'Unnamed: 5' :'Males' ,'Unnamed: 6' :'Females','Unnamed: 8' :'2nd language','Unnamed: 9' :'2nd language Total','Unnamed: 13' :'3rd language','Unnamed: 14' :'3rd language Total' }, inplace=True)
    MN_data.rename(columns={'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM':'State Code','Unnamed: 1':'State','Unnamed: 2':'Lang Code','Unnamed: 3': 'Lang', 'Unnamed: 4' :'Total' ,'Unnamed: 5' :'Males' ,'Unnamed: 6' :'Females','Unnamed: 8' :'2nd language','Unnamed: 9' :'2nd language Total','Unnamed: 13' :'3rd language','Unnamed: 14' :'3rd language Total' }, inplace=True)
    NG_data.rename(columns={'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM':'State Code','Unnamed: 1':'State','Unnamed: 2':'Lang Code','Unnamed: 3': 'Lang', 'Unnamed: 4' :'Total' ,'Unnamed: 5' :'Males' ,'Unnamed: 6' :'Females','Unnamed: 8' :'2nd language','Unnamed: 9' :'2nd language Total','Unnamed: 13' :'3rd language','Unnamed: 14' :'3rd language Total' }, inplace=True)
    MZ_data.rename(columns={'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM':'State Code','Unnamed: 1':'State','Unnamed: 2':'Lang Code','Unnamed: 3': 'Lang', 'Unnamed: 4' :'Total' ,'Unnamed: 5' :'Males' ,'Unnamed: 6' :'Females','Unnamed: 8' :'2nd language','Unnamed: 9' :'2nd language Total','Unnamed: 13' :'3rd language','Unnamed: 14' :'3rd language Total' }, inplace=True)
    Andaman_data.rename(columns={'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM':'State Code','Unnamed: 1':'State','Unnamed: 2':'Lang Code','Unnamed: 3': 'Lang', 'Unnamed: 4' :'Total' ,'Unnamed: 5' :'Males' ,'Unnamed: 6' :'Females','Unnamed: 8' :'2nd language','Unnamed: 9' :'2nd language Total','Unnamed: 13' :'3rd language','Unnamed: 14' :'3rd language Total' }, inplace=True)
    
    df1=AS_data[["State","Lang","Total"]]
    df2=AS_data[["State","2nd language","2nd language Total"]]
    df3=AS_data[["State","3rd language","3rd language Total"]]

    df4=SK_data[["State","Lang","Total"]]
    df5=SK_data[["State","2nd language","2nd language Total"]]
    df6=SK_data[["State","3rd language","3rd language Total"]]

    df7=MG_data[["State","Lang","Total"]]
    df8=MG_data[["State","2nd language","2nd language Total"]]
    df9=MG_data[["State","3rd language","3rd language Total"]]

    df10=TR_data[["State","Lang","Total"]]
    df11=TR_data[["State","2nd language","2nd language Total"]]
    df12=TR_data[["State","3rd language","3rd language Total"]]

    df13=AR_data[["State","Lang","Total"]]
    df14=AR_data[["State","2nd language","2nd language Total"]]
    df15=AR_data[["State","3rd language","3rd language Total"]]

    df16=MN_data[["State","Lang","Total"]]
    df17=MN_data[["State","2nd language","2nd language Total"]]
    df18=MN_data[["State","3rd language","3rd language Total"]]

    df19=NG_data[["State","Lang","Total"]]
    df20=NG_data[["State","2nd language","2nd language Total"]]
    df21=NG_data[["State","3rd language","3rd language Total"]]

    df22=MZ_data[["State","Lang","Total"]]
    df23=MZ_data[["State","2nd language","2nd language Total"]]
    df24=MZ_data[["State","3rd language","3rd language Total"]]

    df25=Andaman_data[["State","Lang","Total"]]
    df26=Andaman_data[["State","2nd language","2nd language Total"]]
    df27=Andaman_data[["State","3rd language","3rd language Total"]]

    df1=df1.dropna()
    df2=df2.dropna()
    df3=df3.dropna()

    df4=df4.dropna()
    df5=df5.dropna()
    df6=df6.dropna()

    df7=df7.dropna()
    df8=df8.dropna()
    df9=df9.dropna()

    df10=df10.dropna()
    df11=df11.dropna()
    df12=df12.dropna()

    df13=df13.dropna()
    df14=df14.dropna()
    df15=df15.dropna()

    df16=df16.dropna()
    df17=df17.dropna()
    df18=df18.dropna()

    df19=df19.dropna()
    df20=df20.dropna()
    df21=df21.dropna()

    df22=df22.dropna()
    df23=df23.dropna()
    df24=df24.dropna()

    df25=df25.dropna()
    df26=df26.dropna()
    df27=df27.dropna()

    df2.rename(columns={'2nd language':'Lang','2nd language Total':'Total'}, inplace=True)
    df3.rename(columns={'3rd language':'Lang','3rd language Total':'Total'}, inplace=True)

    df5.rename(columns={'2nd language':'Lang','2nd language Total':'Total'}, inplace=True)
    df6.rename(columns={'3rd language':'Lang','3rd language Total':'Total'}, inplace=True)

    df8.rename(columns={'2nd language':'Lang','2nd language Total':'Total'}, inplace=True)
    df9.rename(columns={'3rd language':'Lang','3rd language Total':'Total'}, inplace=True)

    df11.rename(columns={'2nd language':'Lang','2nd language Total':'Total'}, inplace=True)
    df12.rename(columns={'3rd language':'Lang','3rd language Total':'Total'}, inplace=True)

    df14.rename(columns={'2nd language':'Lang','2nd language Total':'Total'}, inplace=True)
    df15.rename(columns={'3rd language':'Lang','3rd language Total':'Total'}, inplace=True)

    df17.rename(columns={'2nd language':'Lang','2nd language Total':'Total'}, inplace=True)
    df18.rename(columns={'3rd language':'Lang','3rd language Total':'Total'}, inplace=True)   

    df20.rename(columns={'2nd language':'Lang','2nd language Total':'Total'}, inplace=True)
    df21.rename(columns={'3rd language':'Lang','3rd language Total':'Total'}, inplace=True)   

    df23.rename(columns={'2nd language':'Lang','2nd language Total':'Total'}, inplace=True)
    df24.rename(columns={'3rd language':'Lang','3rd language Total':'Total'}, inplace=True)   

    df26.rename(columns={'2nd language':'Lang','2nd language Total':'Total'}, inplace=True)
    df27.rename(columns={'3rd language':'Lang','3rd language Total':'Total'}, inplace=True)   
    
    North_East_data=pd.concat([df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12,df13,df14,df15,df16,df17,df18,df19,df20,df21,df22,df23,df24,df25,df26,df27])
    North_East_data=North_East_data.drop(["State"],axis=1)
    North_East_data=North_East_data.groupby(North_East_data['Lang'],as_index=False).aggregate({'Total':'sum',}).reindex(columns=North_East_data.columns)
    
    North_East_data=North_East_data[3:]
    
    Sorted_North_East_data=North_East_data.sort_values("Total",ascending=False)
    l=["North-East"]
    for i in range(3):
        temp=Sorted_North_East_data.iloc[i]["Lang"]
        l.append(temp)
    region.append(l)

# Function to find top three most spoken languages in South Region 
def South_Region_Part_b():
    
    KT_data=pd.read_excel('DDW-C17-2900.XLSX')
    # TG = data not available
    AP_data=pd.read_excel('DDW-C17-2800.XLSX')
    TN_data=pd.read_excel('DDW-C17-3300.XLSX')
    KL_data=pd.read_excel('DDW-C17-3200.XLSX')
    Lakshadweep_data=pd.read_excel('DDW-C17-3100.XLSX')
    Puducherry_data=pd.read_excel('DDW-C17-3400.XLSX')

    KT_data.rename(columns={'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM':'State Code','Unnamed: 1':'State','Unnamed: 2':'Lang Code','Unnamed: 3': 'Lang', 'Unnamed: 4' :'Total' ,'Unnamed: 5' :'Males' ,'Unnamed: 6' :'Females','Unnamed: 8' :'2nd language','Unnamed: 9' :'2nd language Total','Unnamed: 13' :'3rd language','Unnamed: 14' :'3rd language Total' }, inplace=True)
    AP_data.rename(columns={'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM':'State Code','Unnamed: 1':'State','Unnamed: 2':'Lang Code','Unnamed: 3': 'Lang', 'Unnamed: 4' :'Total' ,'Unnamed: 5' :'Males' ,'Unnamed: 6' :'Females','Unnamed: 8' :'2nd language','Unnamed: 9' :'2nd language Total','Unnamed: 13' :'3rd language','Unnamed: 14' :'3rd language Total' }, inplace=True)
    TN_data.rename(columns={'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM':'State Code','Unnamed: 1':'State','Unnamed: 2':'Lang Code','Unnamed: 3': 'Lang', 'Unnamed: 4' :'Total' ,'Unnamed: 5' :'Males' ,'Unnamed: 6' :'Females','Unnamed: 8' :'2nd language','Unnamed: 9' :'2nd language Total','Unnamed: 13' :'3rd language','Unnamed: 14' :'3rd language Total' }, inplace=True)
    KL_data.rename(columns={'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM':'State Code','Unnamed: 1':'State','Unnamed: 2':'Lang Code','Unnamed: 3': 'Lang', 'Unnamed: 4' :'Total' ,'Unnamed: 5' :'Males' ,'Unnamed: 6' :'Females','Unnamed: 8' :'2nd language','Unnamed: 9' :'2nd language Total','Unnamed: 13' :'3rd language','Unnamed: 14' :'3rd language Total' }, inplace=True)
    Lakshadweep_data.rename(columns={'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM':'State Code','Unnamed: 1':'State','Unnamed: 2':'Lang Code','Unnamed: 3': 'Lang', 'Unnamed: 4' :'Total' ,'Unnamed: 5' :'Males' ,'Unnamed: 6' :'Females','Unnamed: 8' :'2nd language','Unnamed: 9' :'2nd language Total','Unnamed: 13' :'3rd language','Unnamed: 14' :'3rd language Total' }, inplace=True)
    Puducherry_data.rename(columns={'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM':'State Code','Unnamed: 1':'State','Unnamed: 2':'Lang Code','Unnamed: 3': 'Lang', 'Unnamed: 4' :'Total' ,'Unnamed: 5' :'Males' ,'Unnamed: 6' :'Females','Unnamed: 8' :'2nd language','Unnamed: 9' :'2nd language Total','Unnamed: 13' :'3rd language','Unnamed: 14' :'3rd language Total' }, inplace=True)
    
    df1=KT_data[["State","Lang","Total"]]
    df2=KT_data[["State","2nd language","2nd language Total"]]
    df3=KT_data[["State","3rd language","3rd language Total"]]

    df4=AP_data[["State","Lang","Total"]]
    df5=AP_data[["State","2nd language","2nd language Total"]]
    df6=AP_data[["State","3rd language","3rd language Total"]]

    df7=TN_data[["State","Lang","Total"]]
    df8=TN_data[["State","2nd language","2nd language Total"]]
    df9=TN_data[["State","3rd language","3rd language Total"]]

    df10=KL_data[["State","Lang","Total"]]
    df11=KL_data[["State","2nd language","2nd language Total"]]
    df12=KL_data[["State","3rd language","3rd language Total"]]

    df13=Lakshadweep_data[["State","Lang","Total"]]
    df14=Lakshadweep_data[["State","2nd language","2nd language Total"]]
    df15=Lakshadweep_data[["State","3rd language","3rd language Total"]]

    df16=Puducherry_data[["State","Lang","Total"]]
    df17=Puducherry_data[["State","2nd language","2nd language Total"]]
    df18=Puducherry_data[["State","3rd language","3rd language Total"]]

    df1=df1.dropna()
    df2=df2.dropna()
    df3=df3.dropna()

    df4=df4.dropna()
    df5=df5.dropna()
    df6=df6.dropna()

    df7=df7.dropna()
    df8=df8.dropna()
    df9=df9.dropna()

    df10=df10.dropna()
    df11=df11.dropna()
    df12=df12.dropna()

    df13=df13.dropna()
    df14=df14.dropna()
    df15=df15.dropna()

    df16=df16.dropna()
    df17=df17.dropna()
    df18=df18.dropna()

    df2.rename(columns={'2nd language':'Lang','2nd language Total':'Total'}, inplace=True)
    df3.rename(columns={'3rd language':'Lang','3rd language Total':'Total'}, inplace=True)

    df5.rename(columns={'2nd language':'Lang','2nd language Total':'Total'}, inplace=True)
    df6.rename(columns={'3rd language':'Lang','3rd language Total':'Total'}, inplace=True)

    df8.rename(columns={'2nd language':'Lang','2nd language Total':'Total'}, inplace=True)
    df9.rename(columns={'3rd language':'Lang','3rd language Total':'Total'}, inplace=True)

    df11.rename(columns={'2nd language':'Lang','2nd language Total':'Total'}, inplace=True)
    df12.rename(columns={'3rd language':'Lang','3rd language Total':'Total'}, inplace=True)

    df14.rename(columns={'2nd language':'Lang','2nd language Total':'Total'}, inplace=True)
    df15.rename(columns={'3rd language':'Lang','3rd language Total':'Total'}, inplace=True)

    df17.rename(columns={'2nd language':'Lang','2nd language Total':'Total'}, inplace=True)
    df18.rename(columns={'3rd language':'Lang','3rd language Total':'Total'}, inplace=True)   

    South_data=pd.concat([df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12,df13,df14,df15,df16,df17,df18])
    South_data=South_data.drop(["State"],axis=1)
    South_data=South_data.groupby(South_data['Lang'],as_index=False).aggregate({'Total':'sum',}).reindex(columns=South_data.columns)

    South_data=South_data[3:]
    
    Sorted_South_data=South_data.sort_values("Total",ascending=False)
    l=["South"]
    for i in range(3):
        temp=Sorted_South_data.iloc[i]["Lang"]
        l.append(temp)
    region.append(l)

# Function to find top three most spoken languages in West Region 

def West_Region_Part_b():
    
    RJ_data=pd.read_excel('DDW-C17-0800.XLSX')
    GJ_data=pd.read_excel('DDW-C17-2400.XLSX')
    MH_data=pd.read_excel('DDW-C17-2700.XLSX')
    Goa_data=pd.read_excel('DDW-C17-3000.XLSX')
    Dadra_Nagar_data=pd.read_excel('DDW-C17-2600.XLSX')
    Daman_Diu_data=pd.read_excel('DDW-C17-2500.XLSX')

    RJ_data.rename(columns={'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM':'State Code','Unnamed: 1':'State','Unnamed: 2':'Lang Code','Unnamed: 3': 'Lang', 'Unnamed: 4' :'Total' ,'Unnamed: 5' :'Males' ,'Unnamed: 6' :'Females','Unnamed: 8' :'2nd language','Unnamed: 9' :'2nd language Total','Unnamed: 13' :'3rd language','Unnamed: 14' :'3rd language Total' }, inplace=True)
    GJ_data.rename(columns={'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM':'State Code','Unnamed: 1':'State','Unnamed: 2':'Lang Code','Unnamed: 3': 'Lang', 'Unnamed: 4' :'Total' ,'Unnamed: 5' :'Males' ,'Unnamed: 6' :'Females','Unnamed: 8' :'2nd language','Unnamed: 9' :'2nd language Total','Unnamed: 13' :'3rd language','Unnamed: 14' :'3rd language Total' }, inplace=True)
    MH_data.rename(columns={'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM':'State Code','Unnamed: 1':'State','Unnamed: 2':'Lang Code','Unnamed: 3': 'Lang', 'Unnamed: 4' :'Total' ,'Unnamed: 5' :'Males' ,'Unnamed: 6' :'Females','Unnamed: 8' :'2nd language','Unnamed: 9' :'2nd language Total','Unnamed: 13' :'3rd language','Unnamed: 14' :'3rd language Total' }, inplace=True)
    Goa_data.rename(columns={'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM':'State Code','Unnamed: 1':'State','Unnamed: 2':'Lang Code','Unnamed: 3': 'Lang', 'Unnamed: 4' :'Total' ,'Unnamed: 5' :'Males' ,'Unnamed: 6' :'Females','Unnamed: 8' :'2nd language','Unnamed: 9' :'2nd language Total','Unnamed: 13' :'3rd language','Unnamed: 14' :'3rd language Total' }, inplace=True)
    Dadra_Nagar_data.rename(columns={'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM':'State Code','Unnamed: 1':'State','Unnamed: 2':'Lang Code','Unnamed: 3': 'Lang', 'Unnamed: 4' :'Total' ,'Unnamed: 5' :'Males' ,'Unnamed: 6' :'Females','Unnamed: 8' :'2nd language','Unnamed: 9' :'2nd language Total','Unnamed: 13' :'3rd language','Unnamed: 14' :'3rd language Total' }, inplace=True)
    Daman_Diu_data.rename(columns={'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM':'State Code','Unnamed: 1':'State','Unnamed: 2':'Lang Code','Unnamed: 3': 'Lang', 'Unnamed: 4' :'Total' ,'Unnamed: 5' :'Males' ,'Unnamed: 6' :'Females','Unnamed: 8' :'2nd language','Unnamed: 9' :'2nd language Total','Unnamed: 13' :'3rd language','Unnamed: 14' :'3rd language Total' }, inplace=True)
    
    df1=RJ_data[["State","Lang","Total"]]
    df2=RJ_data[["State","2nd language","2nd language Total"]]
    df3=RJ_data[["State","3rd language","3rd language Total"]]

    df4=GJ_data[["State","Lang","Total"]]
    df5=GJ_data[["State","2nd language","2nd language Total"]]
    df6=GJ_data[["State","3rd language","3rd language Total"]]

    df7=MH_data[["State","Lang","Total"]]
    df8=MH_data[["State","2nd language","2nd language Total"]]
    df9=MH_data[["State","3rd language","3rd language Total"]]

    df10=Goa_data[["State","Lang","Total"]]
    df11=Goa_data[["State","2nd language","2nd language Total"]]
    df12=Goa_data[["State","3rd language","3rd language Total"]]

    df13=Dadra_Nagar_data[["State","Lang","Total"]]
    df14=Dadra_Nagar_data[["State","2nd language","2nd language Total"]]
    df15=Dadra_Nagar_data[["State","3rd language","3rd language Total"]]

    df16=Daman_Diu_data[["State","Lang","Total"]]
    df17=Daman_Diu_data[["State","2nd language","2nd language Total"]]
    df18=Daman_Diu_data[["State","3rd language","3rd language Total"]]

    df1=df1.dropna()
    df2=df2.dropna()
    df3=df3.dropna()

    df4=df4.dropna()
    df5=df5.dropna()
    df6=df6.dropna()

    df7=df7.dropna()
    df8=df8.dropna()
    df9=df9.dropna()

    df10=df10.dropna()
    df11=df11.dropna()
    df12=df12.dropna()

    df13=df13.dropna()
    df14=df14.dropna()
    df15=df15.dropna()

    df16=df16.dropna()
    df17=df17.dropna()
    df18=df18.dropna()

    df2.rename(columns={'2nd language':'Lang','2nd language Total':'Total'}, inplace=True)
    df3.rename(columns={'3rd language':'Lang','3rd language Total':'Total'}, inplace=True)

    df5.rename(columns={'2nd language':'Lang','2nd language Total':'Total'}, inplace=True)
    df6.rename(columns={'3rd language':'Lang','3rd language Total':'Total'}, inplace=True)

    df8.rename(columns={'2nd language':'Lang','2nd language Total':'Total'}, inplace=True)
    df9.rename(columns={'3rd language':'Lang','3rd language Total':'Total'}, inplace=True)

    df11.rename(columns={'2nd language':'Lang','2nd language Total':'Total'}, inplace=True)
    df12.rename(columns={'3rd language':'Lang','3rd language Total':'Total'}, inplace=True)

    df14.rename(columns={'2nd language':'Lang','2nd language Total':'Total'}, inplace=True)
    df15.rename(columns={'3rd language':'Lang','3rd language Total':'Total'}, inplace=True)

    df17.rename(columns={'2nd language':'Lang','2nd language Total':'Total'}, inplace=True)
    df18.rename(columns={'3rd language':'Lang','3rd language Total':'Total'}, inplace=True)   
        
    West_data=pd.concat([df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12,df13,df14,df15,df16,df17,df18])
    West_data=West_data.drop(["State"],axis=1)
    West_data=West_data.groupby(West_data['Lang'],as_index=False).aggregate({'Total':'sum',}).reindex(columns=West_data.columns)
    West_data=West_data[3:]
    
    Sorted_West_data=West_data.sort_values("Total",ascending=False)
    
    l=["West"]
    for i in range(3):
        temp=Sorted_West_data.iloc[i]["Lang"]
        l.append(temp)
    region.append(l)

# Executing above functions to generate outputs

Central_Region_Part_b()
East_Region_Part_b()
North_Region_Part_b()
North_East_Region_Part_b()
South_Region_Part_b()
West_Region_Part_b()

# Writing final results in csv 

with open('region-india-b.csv','w') as out:
    csv_out=csv.writer(out)
    csv_out.writerow(['region', 'language-1', 'language-2', 'language-3'])
    for row in region:
        csv_out.writerow(row)
   
