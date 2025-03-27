import math 
def isPythagoreanTriplet(a,b,c):
    if (pow(a,2)+pow(b,2)==pow(c,2)):
        print("WEEEEEEEEE")
        print(a*b*c)
#isPythagoreanTriplet(96,765,771)
for i in range (1,1001):
    for j in range (1,1001):
        for k in range (1,1001):
            risultato=i+k+j
            if risultato==1000 and isPythagoreanTriplet(i,j,k):
                print("CIAOOOOO L'ho risolto")

