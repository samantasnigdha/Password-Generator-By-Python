import random

upper_case = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lower_case = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['1','2','3','4','5','6','7','8','9','0']
special_case = ['!','@','#','$','%','^','&','(',')']

print("WELCOME TO PSSWORD GENERATOR...")

n_upper = int(input("How many upper case letters do you want in your password? "))
n_lower = int(input("How many lower case letters do you want in your password? "))
num = int(input("How many numbers do you want in your password? "))
n_special = int(input("How many special case letters do you want in your password? "))

plist=[]
for i in range(1,n_upper+1):
    pswd = random.choice(upper_case)
    plist += pswd
for i in range(1,n_lower+1):
    pswd = random.choice(lower_case)
    plist += pswd
for i in range(1,num+1):
    pswd = random.choice(numbers)
    plist += pswd
for i in range(1,n_special+1):
    pswd = random.choice(special_case)
    plist += pswd
random.shuffle(plist)
password=""
for i in plist:
    password += i
print(password)
