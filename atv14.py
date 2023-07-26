#14-Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para 
# o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:
#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$
#Obs.: Salário Bruto - Descontos = Salário Líquido

print("Alo mundo")

ganhoH = float (input("Digite seu ganho por hora: "))
horasT = float (input("Digite suas horas trabalhadas: "))

salario = ganhoH * horasT

sindicato = salario * 0.05
inss = salario * 0.08
impostoR = salario * 0.11

desconto = inss + sindicato + impostoR

liquido = (salario - desconto)

print("Valor descontado do INSS: ", inss, "\n"
"Valor descontado pelo sindicato ", sindicato,
 "\n" "Valor do imposto de renda: ", impostoR, "\n"
  "Seu salário bruto ", salario, "- descontos:", liquido)
