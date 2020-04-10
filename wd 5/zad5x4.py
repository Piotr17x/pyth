class Point:
    counter = []

    def __init__(self, x=0, y=0):
        """Konstruktor punktu."""
        self.x = x
        self.y = y

    def update(self, n):
        self.counter.append(n)

p1 = Point(0,0)
p2 = Point(1,1)
p3 =Point(12,10)
p4=Point(18,2)
print(p3.counter)
print(p4.counter)
p4.update(2)
print(p3.counter)
print(p4.counter)