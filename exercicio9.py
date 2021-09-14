"""
9- Tendo como dados de entrada a altura de uma pessoa,construa um algoritmo que calcule seu peso ideal,
usando a seguinte fórmula: (72.7*altura) - 58:
"""
height = float(input("Digite sua altura:"))
perfect_height = round((72.7 * height) - 58, 2)
print(f"Seu peso ideal é: {perfect_height}")
