dolares = input("Digite el Valor en Dolares: ")
dolares = float(dolares)
valor_peso = 0.000258064
pesos = dolares / valor_peso
pesos = round(pesos, 0)
pesos = str(pesos)
print(str(dolares) + " Dolares, Equivale a: $" + pesos + " Pesos Colombiano")