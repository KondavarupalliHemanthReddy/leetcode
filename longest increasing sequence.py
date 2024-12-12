s=[10,9,2,5,3,7,101,18]
max_count=0
c=1
prev=s[0]
for i in s[1:]:
    if prev>i:
        prev=i
        
    else:
        c+=1
    max_count=max(c,max_count)
print(max_count)