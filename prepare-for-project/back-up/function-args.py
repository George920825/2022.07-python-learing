# 參數預設資料
def power(base=1,exp=0):
    print(base**exp)
power(3,2)
power(5)
# 使用參數名稱對應
def devide(n1,n2):
    print(n1/n2)
devide(2,4)
devide(n2=2,n1=4)
# 無限參數資料(不定)
def avg(*ns):
    sum=0
    for n in ns:
        sum+=n
    print(sum/len(ns))
avg(3,6)
avg(2,8,10,14)
avg(-5,-9,10,2)