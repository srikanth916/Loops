no=int(input("enter a four digit number:"))
print("the given num:")
rev =0
while no !=0:
    r =no%10
    no=no//10
    rev=(rev*10)+r
    print("the rev no", rev)