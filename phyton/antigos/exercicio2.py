n1 = int(input("diga o 1 numero"))
n2 = int(input("diga o 2 numero"))
n3 = int(input("diga o 3 numero"))
n4 = int(input("diga o 4 numero"))
n5 = int(input("diga o 5 numero"))

if n1 > n2 and n1 > n3 and n1 > n4 and n1 > n5:
    print("o numero 1 é o maior")
elif n2 > n3 and n2 > n4 and n2 > n5:
    print("o numero 2 é o maior")
elif n3 > n4 and n3 > n5:
    print("o numero 3 é o maior")
elif n4 > n5:
    print("o numero 4 é maior")
else:
    print("o numero 5 é o maior")