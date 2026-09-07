import pandas as pd
data={
    "name":["Alice","Bob","Charlie","David"],
    "age":[25,30,35,40],
    "salary":[50000,70000,70000,80000]  
}
df=pd.DataFrame(data)
print (df)
#print (df.head())
#print (df.tail())

#print(df.columns)
#print(df.info())
#print (df.shape) #(4,3)
#print (df.dtypes)
#print (df[["name","age","salary"]])
#print(df[df.salary>=60000])
#df["bonus"]=df.salary*0.1
#print(df)
#df["Revised salary"]=df.bonus+df.salary 
#print(df)    
#print(df.isnull().count())
print(df.salary.duplicated())