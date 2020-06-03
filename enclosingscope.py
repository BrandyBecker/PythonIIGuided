x = 100

def outer(x):
    y=50

    def inner():
        print(x,y)
    inner()

outer(75)

#prints: 75  50