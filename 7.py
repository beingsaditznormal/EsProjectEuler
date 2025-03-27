lista = [] 
count=0
x=2
while count<10001 :
    i=2
    cont=0
    while(i<x and cont==0):
        if x % i == 0:
            cont +=1
        i+=1
    if cont==0:
        lista.append(x)
        count+=1
    x+=1

print(lista)
print(len(lista))


'''
lista = []
cont =0 
count=0
x=2
while count<10001 :
    #algoritmo per vedere se il numero
    for i in range(2, x+1):
        if x % i == 0:
            cont +=1
    if cont==1:
        lista.append(x)
        count+=1
    x+=1
    cont=0

print(lista)
print(len(lista))
'''