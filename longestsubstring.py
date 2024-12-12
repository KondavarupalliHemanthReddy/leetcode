s="bbbbbb"
c=0
a=set()
max_s=1
for i in s:
    if i not in a:
        a.add(i)
        c+=1
        print(c)
    else:
        a=set()
        c=1
    max_s=max(max_s,c)
print(max_s)

        
    