def juros(capital, taxa, tempo = 12):
    return (capital * taxa * tempo)/ 100
print("calculo de juros")
cap = float(input("capital "))
tax = float(input("taxa"))
tem = input("tempo (dexe em branxo pq vai se 12 ")
if tem == " ":
    jur = juros(cap, tax)
else:
    tem = float(tem)
    jur = juros(taxa = tax, capital=cap, tempo=tem)
print("o valor dos juros e ", jur)