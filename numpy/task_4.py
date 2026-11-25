
import pandas as pd
"""data={
    "ID":[1, 2, 3, 4,5, 6],
"Name" : ["arun,""Priya",:"Rahul",Divya]

}"""

df= pd.read_csv("employees.csv")
df.head()
df.info()
df.describe()

f=(df[df['salary']>50000 ,['department']=='IT'])
#df.loc
#df.iloc[1:3].values

"""print(df.isna())

print(df.dropna())
df["name"].fillna("shrt")
result=df.groupby("name")["city"]
print(result)"""