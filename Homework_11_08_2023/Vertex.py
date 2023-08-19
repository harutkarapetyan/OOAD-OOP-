class Vertex:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
ls = []

import random
for _ in range(5):
    x = random.randint(-100,100)
    y = random.randint(-100,100)
    obj = Vertex(x,y)
    ls.append(obj)

counter = 1    
for i in ls:
    print(f"Vertex{counter}: x = {i.x}, y = {i.y}")
    counter += 1

