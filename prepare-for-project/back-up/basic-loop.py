# while loop
n=1
sum=0
while n<=10:
    sum+=n
    n+=1
print(sum)
    
# for loop(for x in 列表list; 下方的執行x會分別帶入list中的值)
for x in "Hello":
    print(x)
sum=0
for i in range(11): # range(3)=[0,1,2]; range(3,6)=[3,4,5]
    sum+=i
print(sum)