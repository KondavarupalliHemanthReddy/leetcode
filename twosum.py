a=[2,7,11,15]
d={}
target=9
for i in range(len(a)):
    if target-a[i] in d:
        print(d[target-a[i]],i)
    else:
        d[a[i]]=i
print(d)

       