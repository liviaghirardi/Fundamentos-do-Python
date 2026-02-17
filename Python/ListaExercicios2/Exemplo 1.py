"""
Exemplo de média com formatação na saída
Data: 15/02/2025
Criado por: Lívia Ghirardi do Amaral
Professora: Luciana
"""
#Solicita ao usuário digitar as notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

#PROCESSAMENTO - Calcula a média aritimética
media = (nota1 + nota2 + nota3) / 3.0
#SAÍDA - Exxibe a média formatada
print(f"A média aritimética das notas é {media:.2}")