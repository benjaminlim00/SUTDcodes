class Polynomial:
    def __init__(self, ls):
        self.coeff = ls
        
    def __add__(self, other):
        largest = len(self.coeff)
        largerls = self.coeff[:]
        smaller = other.coeff[:]
        
        if largest < len(other.coeff):
            largest = len(other.coeff)
            largerls = other.coeff[:]
            smaller = self.coeff[:]
            
        for i in range(len(smaller)):
            largerls[i] += smaller[i]
            
        return Polynomial(largerls)
    
    def __sub__(self, other):
        largest = len(self.coeff)
        largerls = self.coeff[:]
        smaller = other.coeff[:]
        
        if largest < len(other.coeff):
            largest = len(other.coeff)
            largerls = other.coeff[:]
            smaller = self.coeff[:]
            
        for i in range(len(smaller)):
            largerls[i] -= smaller[i]
        return Polynomial(largerls)
        
            
            
            
    def __call__(self, x):
        summ = 0
        for i,v in enumerate(self.coeff):
            summ +=  v * x ** i
            
        return summ
            
    def __mul__(self, other):
        m = len(self.coeff) - 1
        n = len(other.coeff) - 1
        result = [0] * (m+n+1)
        for i, c in enumerate(self.coeff):
            for j, d in enumerate(other.coeff):
                result[i+j] += c * d
                
                    
        return Polynomial(result)
    
    def derivative(self):
        ls = self.coeff[:]
        ls1 = []
        del ls[0]
        count = 1
        for item in ls:
            item *= count
            count += 1
            ls1.append(item)
        return Polynomial(ls1)
    
    def differentiate(self):
        ls = self.coeff[:]
        ls1 = []
        del ls[0]
        count = 1
        for item in ls:
            item *= count
            count += 1
            ls1.append(item)
        self.coeff = ls1
        return None
    
#p1 = Polynomial([1, -1])
#p2 = Polynomial ([0 , 1 , 0 , 0 , -6 , -1])
#p3 = p1 + p2
#print(p3.coeff)
#p4 = p1 * p2
#print(p4.coeff)
p4 = Polynomial([1,3,5,7,9])
p5 = p4.derivative()
print(p5.coeff)
        