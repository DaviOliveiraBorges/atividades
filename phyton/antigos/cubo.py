def cubo(num):
    cubo = num * num * num
    print(num, "ao cubo = ", cubo)
n = float(input("fala um n"))
cubo(n)

def cubo(num):
    return num * num * num
n = float(input("fala um n "))
print(n, "ao cubo e ", cubo(n))
print(print(n, "a nona e ", cubo(cubo(n))))