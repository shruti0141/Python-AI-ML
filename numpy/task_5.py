import pandas as pd

csv_data = """order_id, customer_id, amount
1, 101, 500
2, 102,
3, 101,700
4, 103,300
5, 104,900 """

with open("orders.csv", "w") as file:
    file.write(csv_data)

df= pd.read_csv("orders.csv")

#missing values
missing_amount=df.isna().sum()["amount"]
print(missing_amount)