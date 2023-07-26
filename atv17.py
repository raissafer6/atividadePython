#Tempo (em minutos) = (Tamanho do arquivo em bits) / (Velocidade do link em bits por segundo) / 60

arquivoMB = float(input("Digite o tamanho do arquivo para download em MB: "))

velocidadeLink = float(input("Digite a velocidade do link da internet em Mbps: "))

arquivoBits = arquivoMB * 8 * 1024 * 1024

velocidadeBps = velocidadeLink * 1024 * 1024

tempoDownload = arquivoBits / velocidadeBps / 60

print("O tempo de download é aproximadamente: ", round(tempoDownload, 2), "minutos")