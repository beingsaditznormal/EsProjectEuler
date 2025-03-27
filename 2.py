
a=1
b=1
sum =0
while a<4000000:
    current=a
    a=b
    b=current+b
    if(a%2==0):
        sum = sum +a


print(sum)