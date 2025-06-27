km = float(input("quantos km vc rodou? "))
dias = float(input("quantos dias vc alugou? "))

totalkm = km * 0.415
totaldias = dias * 60

totalpagar = totalkm + totaldias

print("voce tera que pagar no total um valor de: ", totalpagar)