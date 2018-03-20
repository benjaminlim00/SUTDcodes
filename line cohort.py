class Line:
    def __init__(self, c0, c1):
        self.c0 = c0
        self.c1= c1
    def __call__(self, x):
        return self.c0 + x * self.c1
    def __str__(self):
        return "The line's parameters are : " + str(self.c1) + ' and ' + str(self.c0)
    def table(self, L, R, n):
        
        out = ''
        interval = (R - L) /  (n-1)
        
        if L == R:
            x = L
            y = self(x)
            return "{:10.2f}{:10.2f}\n".format(x,y)
        
        if n == 0:
            return "Error in printing table"
        
        
        
        for i in range (n):
            x = L + interval * i 
            y = self(x)
            #s = "{x:10.2f}{y:10.2f}\n".format(**{'x':x, 'y':y})
            s = "{:10.2f}{:10.2f}\n".format(x,y)
            out += s
        return(out)
        
    
    
    
line = Line(1,2)
print(line(2))
print(line.table(0, 10, 11))