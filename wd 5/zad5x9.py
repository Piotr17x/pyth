def para(data):
    for id in range(len(data)):
        if id%2==0:
            yield data[id]
sl1=para("kozak")
print(next(sl1))
print(next(sl1))
print(next(sl1))
