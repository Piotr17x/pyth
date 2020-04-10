class para:
    def __init__(self,data):
        self.data=data
        self.lg=len(data)
        self.id=-1
        self.samo=("a","e","i","o","y","u")
    def __iter__(self):
        return self
    def __next__(self):
        if self.id == self.lg:
            raise StopIteration
        self.id = self.id + 1
        if self.data[self.id] in self.samo:
            return self.data[self.id]
        else:
            return next(i)
sl1=para("Grzegorz")
print(isinstance(sl1,para))
i=iter(sl1)
print(next(i))
print(next(i))
