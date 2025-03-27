p=True
i=20
a=20
while (p):
    while i%a==0 and a>=1:
        a=a-1
        print(i,a)
        if(i%a==0 and a==1):
            p=False
    i+=1
    a=20
    