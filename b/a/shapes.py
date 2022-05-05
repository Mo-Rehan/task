
class shapes:
    def __init__(self, a, b=None, c=None):
        
        self.side1=a
        
        self.side2=b
        
        self.side3=c

    def area(self):
        if self.side2==None:
            return self.side1 * self.side1 #square
        if self.side3==None:
            return self.side1 * self.side2 #rectangle
        
        #  calculate the semi-perimeter.
        s = (self.side1 + self.side2 + self.side3) / 2.
        # calculate the area.
        return ((s*(s-self.side1)*(s-self.side2)*(s-self.side3)) ** 0.5)
        
        

