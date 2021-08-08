

i=1
while i<=10:
    print(i*10,end=" ")
    i=i+1




a=[-1,-2,3,4,-6,7]
i=0
b=[]
while i<len(a):
    k=a[i]
    if k<0:
        b.append((-k)*0)
    else:
        b.append(k)
        print(b)
    i=i+1


