def productfun(num):
    list1=list(num)
    mult=1
    for a in list1:
        mult=mult*a
    return mult

n=(2,3,-5)
print("Tuple:",n)

print("product are:",productfun(n))