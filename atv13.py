peso = float(input("Digite o peso de peixes em quilos: "))

pesoLimite = 50

if peso > pesoLimite:
    excesso = peso - pesoLimite
    multa = excesso * 4.00
else: 
    excesso = 0
    multa = 0.00


print("O peso de peixes obtidos é ", peso, " quilos. Sendo o limite de ", pesoLimite, " quilos.")

if excesso > 0:
    print("Há um excesso de peso de ", excesso, " kg. Portanto a multa é de R$", multa)
else:
    print("Não há excesso de peso. Sem multas a pagar.")
