def alphabeticalValue(s):
    s=s.lower()
    ret =0
    for c in s:
        ret+=ord(c)-ord('a')+1
    return(ret)

def NamesScore():
    f = open(r"C:\Users\DAVIDEPEDRETTI\Desktop\22.txt",mode="r", encoding="utf-8")
    names = f.read().split('","')
    names[0]=names[0].replace('"', '')
    names[-1]=names[-1].replace('"', '')
    names.sort()
    ret=0
    for i in range (len(names)):
        ret += (i+1)*alphabeticalValue(names[i])
    
    return (ret)

print(NamesScore())