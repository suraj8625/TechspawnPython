import re
email=input("Enter your email : ")
Reg="(\w+)@(\w+)"
r=re.match(Reg,email)
print("Your company name is : ",r.group(2))