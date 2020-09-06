#----------------ASSIGNMENT 1 DAY 3---------------------


height = int(input("enter the number"))
if height == 1000:
    print("safe land")
elif height>1000 and height<5000:
    print("bring down to 1000")
elif height > 5000:
    print("Turn Around")
else:
    print("Go right position")


#----------------ASSIGNMENT 2 DAY 3---------------------


num = int(input("enter the number"))
if num>1:
    for i in range(2,num):
        if(num%i)==0:
            print(num,"is not a prime number")
            break
    else:
        print(num,"is a prime number")
else:
    print(num,"is not a prime number")






