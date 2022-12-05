import random #pip install random 

pass1= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','@',"#","$","&","`","~","^","!","%","*",">","<","/",":","+","-","?"]

password=""

for x in range(16):
    password=password+random.choices(pass1)[0]

print("Your New Password is :\n ",password)