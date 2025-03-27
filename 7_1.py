lista = []
cont =0 
for x in range(100000):
    #algoritmo per vedere se il numero
    for i in range(2, x+1):
        if x % i == 0:
            cont +=1
    if cont==1:
        lista.append(x)
        
    cont=0

print(lista)
print(len(lista))