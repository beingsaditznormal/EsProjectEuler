def factorial(n):
    fact=1
    for i in range(n,0,-1):
        fact = fact*i
    return fact

def numberToList(numero):
    list = [int(digit) for digit in str(numero)]
    return(list)

def digitFactorials():
    lista=[]
    for i in range(1, 10000000):
        somma=0
        num_list=numberToList(i)
        for j in num_list:
            somma = somma + factorial(j)
            if (somma == i):
                lista.append(i)
                print(i)
    return lista

print(digitFactorials())
