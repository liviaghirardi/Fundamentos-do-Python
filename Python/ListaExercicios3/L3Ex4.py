'''
Escreva um programa que solicite ao usuário dois números e exiba a soma, subtração,
multiplicação e divisão entre eles. Utilize o tipo de dados double.
Data: 15/02/2025
Criado por: Lívia Ghirardi do Amaral
Professora: Luciana
'''

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo núnero: "))

soma = (num1 + num2)
subtracao = (num1 - num2)
multiplicacao = (num1 * num2)
divisao = (num1 / num2)

print("O resultado da soma é: ",soma)
print("O resultado da subtração é: ",subtracao)
print("O resultado da multiplicação é: ", multiplicacao)
print(f"O resultado da divisão é: {divisao:.3}")