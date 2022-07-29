# break
n=0
while n<5:
    if n==3:
        break
    print(n)
    n+=1
print(n)

# continue
n=0
for x in range(4):
    if x%2==0:
        continue
    print(x)
    n+=1
print(n)

# else
sum=0
for n in range(11):
    sum+=n
else:
    print(sum)

# print n^(1/2)
i = int(input("input: "))
for n in range(i):
    if(n*n==i):
        print(n)
        break
else:
    print("Not found.")