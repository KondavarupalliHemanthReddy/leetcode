#solution1
class Solution(object):
    def countSegments(self, s):
        c=0
        prev=' '
        for i in s:
            if i==' ' and prev!=' ':
                c+=1
                prev=i
            else:
                prev=i
        if s=='' or s.count(' ')==len(s) or s[-1]==' ':
            return c
        return c+1
#solution2
#         lis=s.split()
#         return len(lis)
# x=Solution()
# print(x.countSegments("Hello, my name is John"))


        