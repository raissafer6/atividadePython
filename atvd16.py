import math

def calcular_quantidade_latas_galoes(area_pintada, rendimento_lata=18, rendimento_galao=3.6):
    # Considerando 10% de folga
    area_com_folga = area_pintada * 1.1

    # Calcula a quantidade total de litros de tinta necessária
    litros_tinta = area_com_folga / 6

    # Calcula a quantidade de latas e galões necessários (arredondando para cima)
    latas_tinta = math.ceil(litros_tinta / rendimento_lata)
    galoes_tinta = math.ceil(litros_tinta / rendimento_galao)

    return latas_tinta, galoes_tinta

def calcular_preco(latas_tinta, galoes_tinta):
    preco_latas = latas_tinta * 80
    preco_galoes = galoes_tinta * 25

    return preco_latas, preco_galoes

def main():
    try:
        area_pintada = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))

        if area_pintada <= 0:
            print("Por favor, digite um valor positivo para a área a ser pintada.")
            return

        latas_tinta, galoes_tinta = calcular_quantidade_latas_galoes(area_pintada)

        preco_latas, preco_galoes = calcular_preco(latas_tinta, galoes_tinta)

        print("\nOpção 1: Comprar apenas latas de 18 litros")
        print(f"Quantidade de latas de tinta necessárias: {latas_tinta}")
        print(f"Preço total com latas: R$ {preco_latas:.2f}")

        print("\nOpção 2: Comprar apenas galões de 3,6 litros")
        print(f"Quantidade de galões de tinta necessários: {galoes_tinta}")
        print(f"Preço total com galões: R$ {preco_galoes:.2f}")

        # Misturar latas e galões
        latas_mistura = latas_tinta
        galoes_mistura = 0
        preco_mistura = preco_latas

        while latas_mistura > 0:
            latas_mistura -= 1
            galoes_mistura = math.ceil((area_pintada - (latas_mistura * 18 * 6)) / 3.6)
            preco_mistura = (latas_mistura * 80) + (galoes_mistura * 25)

        print("\nOpção 3: Misturar latas e galões")
        print(f"Quantidade de latas de tinta necessárias: {latas_tinta}")
        print(f"Quantidade de galões de tinta necessários: {galoes_mistura}")
        print(f"Preço total com mistura: R$ {preco_mistura:.2f}")

    except ValueError:
        print("Por favor, digite um valor numérico válido para a área a ser pintada.")

if __name__ == "__main__":
    main()
