

a=[1,2,4,6,7,8]
i=1
b=[]
while i<=10:
    if i not in a:
        b.append(i)
    i=i+1
    print(b)  