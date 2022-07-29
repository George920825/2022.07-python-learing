# 載入模組
import pandas as pd

# 建立 Series
data=pd.Series([20, 10, 15])

# basic operate
# print("Max", data.max())
# print("Median", data.median())

# data=data*2
# print(data)

# data=data==20
# print(data)

# 建立 DataFrame
data=pd.DataFrame({
    "name":["Amy", "John", "Bob"],
    "salary":[30000, 50000, 40000]
})

# basic operate
# print(data)
# print(data["name"])
# print(data.iloc[0])