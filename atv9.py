# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

#9-Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))

conta = (5 * ((fahrenheit - 32) / 9))

print("A temperatura em Celsius é igual a", conta)


celsius = float(input("Digite a temperatura em Celsius: "))

resultado = (celsius * (9/5) + 32)

print("A temperatura em Fahrenheit é igual a", resultado)