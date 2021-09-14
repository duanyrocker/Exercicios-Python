"""
12- Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para
o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
- salário bruto.
- quanto pagou ao INSS.
- quanto pagou ao sindicato.
- o salário líquido.
"""
valor_hora = float(input("Por favor digite quanto você ganha por hora:"))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas esse mês:"))
salario = round(valor_hora * horas_trabalhadas, 2)
ir = round((11 * salario) / 100, 2)
inss = round((8 * salario) / 100, 2)
sindicato = round((5 * salario) / 100, 2)
descontos = ir + inss + sindicato
salario_liq = salario - descontos
print(f"sálario bruto : R${salario}\n"
      f"Descontos: Imposto de renda R${ir} \n"
      f"INSS R${inss} \n" f"Sindicato R${sindicato}.\n"
      f"O salario liquido: R${salario_liq}")

