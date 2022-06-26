def loop():
    l = [1,2,3,4]
    for num in l:
        yield num


f = loop()
print(next(f))
print(next(f))
# for r in f:
    # print(r)