import math

def calcular_latas_tinta(area_pintada):
    # Calcula a quantidade de litros de tinta necessária
    litros_tinta = area_pintada / 3

    # Calcula a quantidade de latas de tinta necessárias (arredondando para cima)
    latas_tinta = math.ceil(litros_tinta / 18)

    # Calcula o preço total
    preco_total = latas_tinta * 80

    return latas_tinta, preco_total

def main():
    try:
        area_pintada = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))

        if area_pintada <= 0:
            print("Por favor, digite um valor positivo para a área a ser pintada.")
            return

        latas_tinta, preco_total = calcular_latas_tinta(area_pintada)

        print(f"\nQuantidade de latas de tinta necessárias: {latas_tinta}")
        print(f"Preço total: R$ {preco_total:.2f}")

    except ValueError:
        print("Por favor, digite um valor numérico válido para a área a ser pintada.")

if __name__ == "__main__":
    main()
