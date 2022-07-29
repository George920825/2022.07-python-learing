# 有序可變動列表 list
grades=[12,60,15,70,90]
print(grades)
grades[0]=55
print(grades[0])
grades[1:4]=[]
print(grades[1:4])
grades=grades+[12,65]
print(grades)
print(len(grades))

data=[[3,4,5],[6,7,8]]
print(data[1][2])
data[0][0:2]=[5,5,5]
print(data)

# 有序不可變動列表 tuple
data=(3,4,5)
print(data[2])