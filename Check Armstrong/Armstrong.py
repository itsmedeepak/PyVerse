import math
a=int(input("Enter a number : "))
temp=a
n=len(str(a))
ans=0
while a!=0:
    res = a % 10
    ans += math.pow(res,n)
    a //=10
if(temp==ans):
    print("This number is armstrong")
else:

    print("This is not armstrong")
