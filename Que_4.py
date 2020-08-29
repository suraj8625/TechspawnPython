def pattern(num):
    condition=input("Enter Condition True / False:")
    a="True"
    b="False"
    if(condition==a):
        for i in range(num):
            for j in range(num-i-1):
                print(" ",end="")
            for j in range(2*i+1):
                print("*",end="")
            print("\n")
    elif(condition==b):
        for i in range(num):
            for j in range(i):
                print(" ",end="")
            for j in range(2*(num-i)-1):
                print("*",end="")
            print("\n")
    else:
        print("Enter proper condition ")
        print("Tip: Condition is case sensitive")
pattern(5)