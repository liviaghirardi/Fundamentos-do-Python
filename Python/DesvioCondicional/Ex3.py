"""
DESVIO CONDICIONAL ANINHADO (1)
Verifique se o número digitado é positivo, negativo ou igual a zero.


Data: 15/02/2025
Criado por: Lívia Ghirardi do Amaral
Professora: Luciana
"""

num = int(input("Digite o número: "))

if num > 0:
    print("Número possitivo!")
else:
    if num < 0:
        print("Número negativo!")
    else:
        print("Número igual a zero!")

"""
SINTAXE DO DESVIO CONDICIONAL ANINHADO
if_teste_logico1
    instrucao_se_for_verdadeira
else:
    intrucao_se_falsa2
"""