nums =[12,93,-90,-9,75,-19,3,-10,-93,-68,-97,88,-90,23,36,-82,24,-54,-99,40,9,-10,-93,20,55,-60,69,3,64,52,-18,-60,44,-97,58,97,94,76,8,87,25,-2,-15,23,-73,64,80,19,30,-67,-68,-32,-10,53,-88,-71,-26,-32,21,78,-33,-43,35,-32,-84,-65,63,55,-21,-85,41,-98,16,39,-78,74,44,-77,8,74,16,41,-3,-7,-10,29,-28,-53,48,60,6,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000,-1000000000]
lower = -124
upper = 108
nums.sort()
c=0
i=0
j=len(nums)-1
while(i<j):
    sum1=nums[i]+nums[j]
    if sum1>upper:
        j-=1
    elif sum1<lower:
        i+=1
    else:
        l=j
        while i<l and lower<=(nums[i]+nums[l])<=upper:
            c+=1
            l-=1
        i+=1
        
print(c)
    