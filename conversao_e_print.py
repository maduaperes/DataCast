#Conversão de valores primitivos -> Entendendo os tipos de dados em Python (DECIMAL, BINÁRIO, OCTAL, HEXADECIMAL)

"""
- 2 em valor de caractere 0011 0010
- 2 em valor numérico 0000 0010
- 0 0 0 0 0 0 0 1 0 -> Binário
- 128,64,32,16,8,4,2,1 -> Decimal

BIN - DEC
00000000 = 0
00000001 = 1
00000010 = 2
00000100 = 4
00001000 = 8
1 + 2 = 3, ou seja 00000011 = 3
"""


texto="2"
#texto = "2" → string contendo "2"

texto1=str(2)
#texto1 = str(2) → inteiro 2 convertido para string "2"

numero=3
#numero = 3 → inteiro 3

numero1=int(3)
#numero1 = int(3) → inteiro 3 (mesmo valor, usando int())

numero2=float(3)
#numero2 = float(3) → float 3.0 (inteiro convertido para decimal)


print(texto)
print(texto1)
print(numero)
print(numero1)
print(numero2)

#Concatenação de texto e variavel no print
nome = input("Digite seu nome: ")
print("Olá "+nome+" \nBem vindo(a) ao Python!")

#Concatenação de texto e fórmula no print
valor_uni = float(input("Informe o valor unitário: "))
quantidade = int(input("Informe a quantidade: "))
print("O valor total é: ", valor_uni*quantidade)