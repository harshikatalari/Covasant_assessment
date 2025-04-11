# Question-5:

# from pkg.poly import Poly 
# a = Poly(1,2,3)  #an, ...., a0 
# b = Poly(1,0,1,1,2,3)
# c = a+b 
# print(c) #Poly ( 1,0,1, 2,4,6)

class Poly:
    def __init__(self,*nums):
        self.nums=list(nums)
        
    def __add__(self,other):
        
        max_len=max(len(self.nums),len(other.nums))
        output=[0]*max_len
        
        for i in range(1, max_len+1):
            
            val1 = self.nums[-i]  if i <= len(self.nums) else 0
            val2=other.nums[-i] if i<= len(other.nums) else 0
            output[-i] += val1 + val2
        
        return output

a=Poly(1,2,3)
b=Poly(1,0,1,1,2,3)
c=a+b
print(c)