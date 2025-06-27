while True:
    try:
        print("fala um numero")
        n1 = float(input("n1 "))
        n2 = float(input("n2 "))
        r = n1 / n2
        print(n1, "/", n2, "=", r)
        break
    except ValueError as e:
        print(e)
        print("Numero invalido", type(e))
    except ZeroDivisionError as e:
        print("dovizao por zerp")
    print(n1, "/", n2, "=", r)

