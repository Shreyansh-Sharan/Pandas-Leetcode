"""
#    +-------------+---------+
#| Column Name | Type    |
#+-------------+---------+
#| id          | int     |
#| name        | varchar |
#| salary      | int     |
#| managerId   | int     |
#+-------------+---------+
#id is the primary key (column with unique values) for this table.
#Each row of this table indicates the ID of an employee, their name, salary, and the ID of their manager.
# 

#Write a solution to find the employees who earn more than their managers.

#Return the result table in any order.

#The result format is in the following example.
#*/

"""
import pandas as pd
employee = pd.DataFrame

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
  pd1 = employee.merge(employee,left_on="managerId",right_on="id", suffixes=['_e',"_m"],how="inner")
  ### Filter to be applied before chaining
  
  # filter1 = pd1['salary_m'] < pd1['salary_e']
  # new_pd = pd1[filter1]
  # new_pd = new_pd[['name_e']]
  
  ### The above three commands are chained together in below line
  new_pd = pd1[pd1['salary_m'] < pd1['salary_e']] [['name_e']]
  new_pd.rename(columns = {'name_e':'Employee'},inplace= True)
  return new_pd