class MySquareCircle():
    pi = 3.14
    
    def __init__(self,length,breadth,radius):
        #Assign and initialize vairables
        
        self.length = length
        self.breadth = breadth
        self.radius = radius
        
    def Circumference(self):
        return self.pi * self.radius * 2
    
    def Circlearea(self):
        return self.pi * self.radius * self.radius 
    
    def Squarearea(self):
        area = self.length * self.breadth
        if self.length == self.breadth:
            print("Since the length and breadth are equal, its a square {}".format(self))
        else:
            print("The given measurement is a rectangle {}".format(area))
