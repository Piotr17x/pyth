def fib(ile):
    i=0
    j=1
    pom=0
    for n in range(ile):
        yield j
        pom=i
        i=j
        j+=pom
cig=fib(20)
for n in range(20):
    print(next(cig))