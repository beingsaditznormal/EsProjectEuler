def sumDivisors(numero):
    somma=0
    num=int((numero/2))
    for i in range(1,num+1):
        if(numero%i==0):
            #print(i)
            somma +=i
    return(somma)
#print(sumDivisors(220))

def amicableNumbers():
    somma=0
    diz=[]
    for i in range(1,10000):
        if sumDivisors(i)>i and sumDivisors(i)<10000:
            if sumDivisors(sumDivisors(i))==i:
                diz.append((i,sumDivisors(i)))
                somma+=i+sumDivisors(i)
    print(somma)
    return(diz)
    #return(somma)
    #print(somma)
print(amicableNumbers())
    

