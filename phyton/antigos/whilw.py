soma = 0

while True:
    n = float(input("nmero "))
    if n < 0:
        continue
    if n == 0:
        break
    soma = soma + n
print("soma dos n = ", soma)