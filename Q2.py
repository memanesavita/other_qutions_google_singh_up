
from typing import Counter


# vowel=input("eter the vowel and consonunt")
# count=0
# if (vowel == "a") or (vowel == "i") or (vowel == "o")or (vowel=="u")or(vowel=="e"):
#     count=count+1
#     print("it is a vowel")
# else:
#     print("it is a consonunt")




    
vcount = 0;  
# count = 0;  
str = input("enter a name: ")
       
    #Converting entire string to lower case to reduce the comparisons  
str = str.lower();  
for i in range(0,len(str)):   

    if str[i] in ('a',"e","i","o","u",): 
        print(str[i],"vowel") 
        # count = count + 1;  
    elif (str[i] >= 'a' and str[i] <= 'z'):  
        # ccount = ccount + 1;
        print(str[i],"cosonunt")










    

        
















