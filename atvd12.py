def calcular_peso_ideal(altura, sexo):
    if sexo == 'masculino':
        peso_ideal = (72.7 * altura) - 58
    elif sexo == 'feminino':
        peso_ideal = (62.1 * altura) - 44.7
    else:
        raise ValueError("Sexo inválido. Insira 'homem' ou 'mulher'.")

    return peso_ideal

# Exemplo de uso:
altura_pessoa = float(input("Digite a altura da pessoa em metros: "))
sexo_pessoa = input("Digite o sexo da pessoa (masculino/feminino): ")

peso_ideal = calcular_peso_ideal(altura_pessoa, sexo_pessoa)

print(f"O peso ideal para uma pessoa de {altura_pessoa:.2f} de altura e do sexo {sexo_pessoa} é: {peso_ideal:.2f} kg.")
