





from os import write


question=input("do you have an account(yes/no:")
if question=="y"or question=="Y" or question=="yes":
    my_file=open("new_login.""txt","r+")
    f=my_file.read()
    name=input("enter username:")
    lastname=input("enter the lasname:")
    password=input("enter the password:")
    if name in f and password in f:
        print("login successfully")
    else:
        print("sorry invalid fist username and pasword ")
    my_file.close()

else:
    ("you have all ready account")    
# my_file.close()
if question=="n"or question=="N"or question=="no":
    num=input("DO YOU WANT TO SINGH UP NEW ACCOUNT(YES/NO)")
    if num=="yes" or num=="yes":
        file =open("new_login.txt","w")
        firs_name=input("enter the new username:")
        file.write(firs_name)
        

        # firs_name=input("enter the firs name")
        # file,write("first nam")

        lastname=input("enter the lastname:")
        file.write(lastname)
        
        password=input("enter the password:")
        file.write(password)
        print("YOUR NEW ACCOUNT IS CREATED SUCCESSFULY")
        file.close()






























