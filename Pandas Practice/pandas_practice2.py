#rename

import pandas as pd
data={
    "name":["Alice","Bob","Charlie","David"],
    "age":[25,30,35,40],
    "salary":[50000,70000,70000,80000]  
}
df=pd.DataFrame(data)
print (df)
df=df.rename(columns={"name":"Empname","age":"empage","salary":"empsalary"})

print("After rename \n ",df)
print(df.columns)
