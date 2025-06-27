print("dois numeros")
n1 = int(input("n1 "))
n2 = int(input("n2 ",),)

if n1 < 1 or n2 < 1:
    print("numeros invalidos")
else:
    while True:
        resto = n1%n2
        print(n1, "/", n2, "-> resto: ", resto)
        if resto == 0:
            break
        n1 = n2
        n2 = resto
print("o mdc é ", n2)