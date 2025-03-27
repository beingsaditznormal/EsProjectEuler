num = int(600851475143)
print(type(num))

for i in range(1,num+1):
    if(num%i==0):
        cont =0
        for j in range(1, i):
            if i % j == 0:
                cont +=1
        if cont==1:
            print(i,"è divisore primo")

