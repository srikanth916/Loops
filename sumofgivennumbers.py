no = int(input("enter a four digit number"))
sum =0
while no!=0:
    r=no%10
    no =no//10
    sum +=r
    print( sum)