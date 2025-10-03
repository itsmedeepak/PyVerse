a=int(input("Enter your number : "))
print(f"factors of {a} are : ")
n=int(a/2)
for i in range(1,n+1):
    if(a%i==0):
        print(i)
print(f"factor of {a}")
