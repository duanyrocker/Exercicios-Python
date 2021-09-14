"""
10- Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule
seu peso ideal, utilizando as seguintes fórmulas:
- Para homens: (72.7*h) - 58
- Para mulheres: (62.1*h) - 44.7
"""
height = float(input("Por favor digite a altura:"))
sex = int(input("Escreva um número para informar o sexo: 1- masculino ou 2 - mulheres:"))
weigth = float(input("Digite o peso:"))
if sex == 1:
    weight_men = round((72.7 * height) - 58, 2)
    if weigth == weight_men:
        print(f"Seu peso perfeito é: {weight_men},voce está com peso ideal")
    elif weigth < weight_men:
        print(f"Seu peso perfeito é: {weight_men},você está acima do peso")
    else:
        print(f"Seu peso perfeito é: {weight_men},você está abaixo do peso")
if sex == 2:
    weight_woman = round((62.1 * height) - 44.7, 2)
    if weigth == weight_woman:
        print(f"Seu peso perfeito é: {weight_woman},você está com peso ideal")
    elif weigth < weight_woman:
        print(f"Seu peso perfeito é:{weight_woman}, você está acima do peso")
    else:
        print(f"Seu peso perfeito é: {weight_woman}, você está abaixo do peso")
