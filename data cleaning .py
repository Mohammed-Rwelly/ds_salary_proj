import pandas as pd
data=pd.read_csv('glassdoor_jobs.csv')
print(data.columns)
#as we can see above in row 24 the salary is equal -1 this is wrong ,So we are Removing  job postings with salary is equal -1.
data=data[data['Salary Estimate'] != '-1']
salary =data['Salary Estimate'].apply(lambda x:x.split('(')[0])