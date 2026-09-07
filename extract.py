import pandas as pd
data=pd.read_csv("employees.csv")
print(data)
#print("Head is \n ",data.head())
#print("tail is \n ",data.tail())
#print("columns are \n ",data.columns)
print(data.salary)
print(data['salary'])
print(data[data.salary>55000])

