#Tomo lanche todas as noites na faculdade, de segunda a sexta. Faça
#um código, usando contadores e acumuladores, que calcule quanto gasto por semana.

x = 1
soma = 0

while x <= 5:
    dias = int(input("Valor gasto: R$: " ))
    soma = soma + dias
    x = x + 1
    print("Gasto na semana: R$" ,soma)


