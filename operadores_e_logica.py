#Operadores matemáticos - Aritméticos

print("\nOperadores matemáticos - Aritméticos:\n")
a = 10
b = 5
print(a**b) #Potência
print(a**(1/2)) #Raiz
print(a*b) #Mult
print(a/b) #Div
print(a//b) #Div int
print(a%b) #Mod Rest
print(a+b) #Soma
print(a-b) #Sub
print((a+a)*b) #Prioridade


#Operadores Relacionais
print("\nOperadores Relacionais:\n")
print(2==2)
print(2>=2)
print(2<=2)
print(2!=2)
print(2>2)
print(2<2)


#Operadores Lógicos
print("\nOperadores Lógicos:\n")
x = False
y = False

print(x and y)
print(x or y)
print(x or not y)

#Operadores Combinados
print("\nOperadores Combinados:\n")
num1 = 4
num2 = 2
num3 = 4
num4 = 2

num3 = num3 % num4
num1%=num2
print(num1)
print(num2)
print(num3)
print(num4)

"""
Todos precisam ser falsos para se obter uma resposta falsa, caso contrário, verdadeiro

Ex:

V  V  V - V
V  F  F - V
F  V  F - V
F  F  F - F

(Remover comentário "#", seleciona a variável/função e aperta "ctrl" + ";")
"""