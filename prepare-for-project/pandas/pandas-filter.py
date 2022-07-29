import pandas as pd

# data=pd.Series([30, 15, 20])
# # condition=[True, False, True]
# condition=data>18
# filteredData=data[condition]
# print(filteredData)

# data=pd.Series(["您好", "Python", "Pandas"])
# # condition=[True, False, True]
# condition=data.str.contains("P")
# filteredData=data[condition]
# print(filteredData)

data=pd.DataFrame({
    "name":["Amy", "Bob", "Charles"],
    "salary":[30000, 50000, 40000]
})
# print(data)
# condition=[False, True, True]
condition=data["name"]=="Amy"
# condition=data["salary"]>=40000
print(condition)
filteredData=data[condition]
print(filteredData)