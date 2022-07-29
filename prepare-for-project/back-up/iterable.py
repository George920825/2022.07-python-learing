# 字串 列表 集合 字典

# for 變數名稱 in 可疊代資料
dic={"abc":1,"d":3,"3":5,"13":7}
for key in dic:
    print(key)
    print(dic[key])

# 內建函式
result=max([10,2,45,3])
print(result)
result=max("xks")
print(result)
result=max({10,200,30,4})
print(result)
result=={"abc":1,"d":3,"3":5,"13":7}
print(result)

result=sorted("cab")
print(result)
result=sorted({-10,200,30,-4})
print(result)