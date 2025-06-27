numeros_extenso = (
    "zero", "um", "dois", "três", "quatro", "cinco",
    "seis", "sete", "oito", "nove", "dez", "onze",
    "doze", "treze", "quatorze", "quinze", "dezesseis",
    "dezessete", "dezoito", "dezenove", "vinte"
)

numero = int(input("Digite um número entre 0 e 20: "))

if 0 <= numero <= 20:
    print("Número por extenso: ", numeros_extenso[numero])
else:
    print("Número inválido.")