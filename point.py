class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return("hello")
        
    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

my_point = Point(3, 5)
print(my_point)