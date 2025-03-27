def isPalindrome(n):
    p=True
    l=len(n)
    for i in range (0,l):
        if n[i]!=n[len(n)-1-i]:
            p=False
    
    return(p)

listPalindromi=[]
for i in range(100,1000):
    for j in range(100,1000):
        if isPalindrome(str(i*j)):
            print(i*j, i, j)
            listPalindromi.append(i*j)

print(max(listPalindromi))
