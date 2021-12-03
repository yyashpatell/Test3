class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def getPerimeter(self):
        return 2* (self.length + self.width)
        
    def getArea(self):
        return (self.length * self.width)

L = int(input("please enter the length of rentangle: "))
W = int(input("please enter the width of rentangle: "))
R1 = Rectangle(L,W)
print("area of rectangle is: ", R1.getArea())
print("perimeter of rectangle is: ", R1.getPerimeter())

    






        
    

        

        
        






    
