s=[9,8,7,6,5,4,7,2,1,0]
max_count=0
c=1
prev=s[0]
dp=[]
for i in s[1:]:
    if i<prev:
        c+=1
        prev=i
    else:
        c=1
        prev=i
    max_count=max(c,max_count)
    dp.append(max_count)
print(dp)
