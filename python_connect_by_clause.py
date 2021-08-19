# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 14:49:12 2021

@author: Michael Yonas
#find the hierarchy queries using recursive function in Python
#try to achive the oracle connect by clause function
select EMPLOYEE_ID,FIRST_NAME,MANAGER_ID
from hr.employees
start with MANAGER_ID =100
connect by prior employee_id = MANAGER_ID
 
"""
#import the pandas packages
# to read the data from employees
import pandas as pd
df = pd.read_csv(r'C:\Users\Michael Yonas\Downloads\table.csv')
print(df.head(10))

#declare the varaibels
#write recursive functions
final_list=[]
dfs=[]
def get_parent_child_dtls(manager_id,level,sub_manager_list=[]):
    emp_list2=[]
    if level == 1:
        print(level)
        df1=df.query('MANAGER_ID == @manager_id')[['EMPLOYEE_ID','FIRST_NAME','MANAGER_ID']]
        #print(df.query('MANAGER_ID == @manager_id')[['EMPLOYEE_ID','FIRST_NAME','MANAGER_ID']])
        final_df = pd.DataFrame(df1, columns =['EMPLOYEE_ID','FIRST_NAME','MANAGER_ID'])
        #print(final_df)
        dfs.append(final_df)
        emp_list=[]
        emp_list = list(df1['EMPLOYEE_ID'])
        #print(emp_list)
        level = level + 1
        get_parent_child_dtls(manager_id,level,emp_list)
    elif level > 1:
        #print(level)
        level = level + 1
        employee_ids=''
        for emp in sub_manager_list:
            sub_manager=str(emp)
            #print(df.query('MANAGER_ID == @sub_manager')['EMPLOYEE_ID','FIRST_NAME','MANAGER_ID']])
            #return_df=return_df.append(df.query('MANAGER_ID == @sub_manager')[['EMPLOYEE_ID','FIRST_NAME','MANAGER_ID']])
            #add_managers_df(final_df,df.query('MANAGER_ID == @sub_manager')[['EMPLOYEE_ID','FIRST_NAME','MANAGER_ID']])
            #print(df.query('MANAGER_ID == @sub_manager')[['EMPLOYEE_ID','FIRST_NAME','MANAGER_ID']])
            dfs.append(df.query('MANAGER_ID == @sub_manager')[['EMPLOYEE_ID','FIRST_NAME','MANAGER_ID']])
            employee_ids=list(df.query('MANAGER_ID == @sub_manager')['EMPLOYEE_ID'].values)
            for child_emp in employee_ids:
                emp_list2.append(child_emp)
                print(child_emp)
        print('length---' + str(len(emp_list2)))
        print(emp_list2)
        if len(emp_list2)>0:
            get_parent_child_dtls(manager_id,level,emp_list2)
        else:
             result = pd.concat(dfs)
             #print(result)
             return result

#calling the functions
get_parent_child_dtls('100',1)
result = pd.concat(dfs,ignore_index=True)
print(result)
