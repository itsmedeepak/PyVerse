a=int(input("Enter a number : "))
print(f"factors of {a} are : ")
for i in range(a):
    if(a%i==0):
        print(i)
