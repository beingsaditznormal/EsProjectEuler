def numberToList(numero):
    list = [int(digit) for digit in str(numero)]
    return(list)
def Potenza(list,numero):
    sum=0
    #flag = True
    for i in (list):
        sum = sum + (i**5)
        #print (i,sum)
    #return(sum)
    if sum == numero: 
        return(True)
    else:
        return(False)

lista2=[]
for i in range(1,1000000):
    lista=numberToList(i)
    flag = Potenza(lista,i)
    if flag:
        lista2.append(i)
print(lista2)
somma = 0
for j in lista2:
    somma += j
print(somma)

#print(Potenza(numberToList(1634),1634))