def distinctPowers():
    lista=[]
    for a in range(2,101):
        for b in range(2,101):
            num = a**b
            if num not in lista:
                lista.append(num)
    lista.sort()
    count=0
    for i in lista:
        count+=1
    #return(lista.count(value=any))
    print(count)
print(distinctPowers())