

def StringCount(string):
    d={}
    l=[]
    for i in string:
        d[i]=d.get(i,0)+1
    for v in d.values():
        l.append(v)
    if len(set(l))==1:
        return True
    else:
        return False

print(StringCount("aaabbb"))
