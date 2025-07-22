class Solution(object):
    def plusOne(self, digits):
        if digits[-1]<9:
            digits.append(digits[-1]+1)
            digits.pop(-2)
        else:
            sum=''
            for i in digits:
                sum+=str(i)
            sum=int(sum)+1
            digits=[]
            for i in  str(sum):
                digits.append(int(i))
        return digits
