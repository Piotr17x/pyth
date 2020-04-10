class para:
    def __init__(self,data):
        self.data=data
        self.lg=len(data)
        self.id=-2
    def __iter__(self):
        return self
    def __next__(self):
        if self.id == self.lg:
            raise StopIteration
        self.id = self.id + 2
        return self.data[self.id]
sl1=para("kozak")
i=iter(sl1)
print(next(i))
print(next(i))
print(next(i))
