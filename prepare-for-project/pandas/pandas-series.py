# 載入模組
import pandas as pd
# 資料索引
# data=pd.Series([5, 4, -2, 3, 7], index=["a", "b", "c", "d", "e"])
# print(data)
# 觀察資料
# print("資料型態",data.dtype)
# print("資料數量",data.size)
# print("資料索引",data.index)
# 取得資料
# print(data[2], data[0])
# print(data["e"], data["d"])
# 數字運算
# print(data.max(), data.sum(), data.std(), data.mean(), data.median())
# print(data.nlargest(3))
# print(data.nsmallest(2))

data=pd.Series(["您好", "Python", "PANDAS"])
# print(data.str.lower())
# print(data.str.len())
# print(data.str.cat(sep="-"))
# print(data.str.contains("P"))
# print(data.str.replace("您好", "Hello"))