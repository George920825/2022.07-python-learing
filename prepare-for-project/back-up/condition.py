# 判斷式
x=int(input("請輸入數字: ")) # get string and cast into int
y=50
if x>y:
    print("Greater than 50.")
elif x==y:
    print("Equal to 50.")
else:
    print("Less than 50")

# 四則運算
n1=int(input("請輸入數字一: "))
n2=int(input("請輸入數字二: "))
op=input("請輸入運算: +, -, *, /: ")
if op=="+":
    print(n1+n2)
elif op=="-":
    print(n1-n2)
elif op=="*":
    print(n1*n2)
elif op=="/":
    print(n1/n2)
else:
    print("不支援的運算")