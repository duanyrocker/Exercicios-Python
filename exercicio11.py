"""
11- João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário
de seu trabalho.Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do
estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
João precisa que você faça um programa que leia a variável peso (peso de peixes) e
calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na
variável multa o valor da multa que João deverá pagar.
Imprima os dados do programa com as mensagens adequadas.
"""
peso_limite = 50
multa = 4
peso = float(input("Por favor,digite o valor do peso para verificar:"))
if peso > peso_limite:
    excesso = peso - peso_limite
    resultado = excesso * multa
    print(f"O peso informado está acima.Valor da multa: R${resultado}")
else:
    print(f"O peso informado está dentro do regulamento")
