#10-Faça um Programa que peça 2 números inteiros e um número real. 
# Calcule e mostre: 
# o produto do dobro do primeiro com metade do segundo . 
# a soma do triplo do primeiro com o terceiro. 
# o terceiro elevado ao cubo.

print("Alo mundo")

numI = int (input("Digite um número inteiro: "))
numR = float (input("Digite um número real: "))
numID = (numI * 2) + (numR /2)
numTIR =(numI * 3) + (numR * 3)
numF = numTIR * numTIR
print("Dobro de ", numI, " com metade do ", numR, ":", numID,"\n"
"A soma do triplo de ", numI ,"com ", numID, ":", numTIR, "\n",
"O número", numID ," elevado ao cubo : ", numF)