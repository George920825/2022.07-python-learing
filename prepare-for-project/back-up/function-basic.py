# define
def multipy(m,n):
    print(m*n)
# call
print(multipy(7,9))

# define
def multipy(m,n):
    return m*n
# call
print(multipy(8,10)+multipy(1,3))

# 包裝
sum=0
for n in range(1,11):
    sum+=n
print(sum)
#
def calculate(m):
    sum=0
    for n in range(1,m+1):
        sum+=n
    return sum

print(calculate(10))