# 載入模組
from operator import index
import pandas as pd

# 資料索引: pd.DataFrame(字典, index=索引列表)
data=pd.DataFrame({
    "name":["Amy", "Bob", "Charles"],
    "salary":[30000, 50000, 40000]
}, index=["a", "b", "c"])
print(data)
print("============")

# 觀察資料
# print("資料數量",data.size)
# print("資料形狀(列,欄)",data.shape)
# print("資料索引",data.index)

# 取得列 (Row/橫) 的 Series 資料: 根據順序、索引
# print("第二列", data.iloc[1], sep="\n")
# print("============")
# print("列a", data.loc["a"], sep="\n")

# 取得欄 (Column/直) 的 Series 資料: 根據欄位名稱
# print("name欄位", data["name"], sep="\n")
# names=data["name"] # 取得單維度的 Series 資料
# print(names.str.upper(), sep="\n")
saleries=data["salary"]
print("salary mean:", saleries.mean())

# 建立新欄位
data["revenue"]=[500000, 400000, 300000] # data[新欄位名稱]=列表
data["rank"]=pd.Series([3,6,1], index=["b", "a", "c"])
data["cp"]=data["revenue"]/data["salary"]
print(data)