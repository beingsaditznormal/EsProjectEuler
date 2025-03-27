i=20
j=1
bool = True
while True:
    while j<21 and bool==False:
        if(i%j==0):
            bool=False
        else:
            bool=True
        j+=1
    i=i+1
print(i)
    