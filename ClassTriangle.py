# TASK: implement the Triangle class as described in the Quiz paper

class Triangle:
    def __init__(self, color = 'green', filled = True, side1 = 1.0, side2 = 1.0, side3 = 1.0):
        self.color = color
        self.filled = filled
        self._side1 = side1
        self._side2 = side2
        self._side3 = side3
        
    def get_side1(self):
        return self._side1
    
    def get_side2(self):
        return self._side2
    
    def get_side3(self):
        return self._side3
    
    def set_side1(self, value):
        if value >= 0:
            self._side1 = value
        return self._side1
    def set_side2(self, value):
        if value >= 0:
            self._side2 = value
        return self._side2
    def set_side3(self, value):
        if value >= 0:
            self._side3 = value
        return self._side3
        
    side1, side2, side3 = property(get_side1, set_side1), property(get_side2, set_side2), property(get_side3, set_side3)