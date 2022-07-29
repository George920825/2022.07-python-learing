# 集合的運算
s1={3,4,5}
print(3 in s1)
print(10 not in s1)
s2={4,5,6,7}
s3=s1&s2 # 交集: &
s3=s1|s2 # 聯集: | (不會重複取)
s3=s1-s2 # 差集: - (s1減去和s2重複的部分)
s3=s1^s2 # 反交集: ^ (取不重複的)
print(s3)
s=set("Hello") # set(字串)(不會重複取)
print(s)
print("H" not in s)

# 字典的運算
dic={"apple":"蘋果","bug":"蟲蟲"}
dic["apple"]="小蘋果"
print(dic["apple"])
print("apple" in dic) # 判斷key是否存在
print(dic)
del dic["apple"] # delete key-value pair in dictionary
print(dic)
dic={x:x*2 for x in [3,4,5]} # make dictionary from set
print(dic)