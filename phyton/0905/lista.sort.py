numeros = [11, 12,32,543,23,675,1,2,96,45]
print("lista original")
for n in numeros:
    print(n, end=" ")
print("\n_______________________________-")
print("lista crescente: ")
numeros.sort()
for n in numeros:
    print(n, end= " ")
print("\n _______________________")
print("lista decrescente")
numeros.sort(reverse=True)
for n in numeros:
    print(n, end=" ")
print("\n_______________________________-")


print("maior numero: ", max(numeros))
print("menor m=numero", min(numeros))
print("soma de todos os numeros ", sum(numeros))