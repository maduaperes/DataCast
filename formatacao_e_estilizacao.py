# """
# Arredondamento de números:
# Para arredondar números ao exibir, você pode utilizar a função round() 
# ou a formatação de strings do Python.   
# """
# Cria duas variáveis com números de ponto flutuante (decimais)
num1 = 3.14159
num2 = 2.71828

# Arredonda a variável num1 para ter apenas 2 casas decimais
print(round(num1, 2))  
# Saída: 3.14

# Arredonda a variável num2 para ter 3 casas decimais
print(round(num2, 3))  
# Saída: 2.718

# Usando formatação de strings para o arredondamento (o f significa float)
print("{:.2f}".format(num1))  
# Saída: 3.14

print("{:.3f}".format(num2))  
# Saída: 2.718

# """
# Quebra de linha:
# Para pular linhas, você pode utilizar o caractere especial de escape \n ou 
# usar a opção end do print para definir o caractere a ser usado no final da saída.
# """
# Usando \n para forçar o texto a pular para a linha de baixo no meio da frase
print("Linha 1\nLinha 2")
# Saída: 
# Linha 1
# Linha 2

# Usando a opção 'end' para alterar o final do print (neste caso, adiciona duas quebras de linha ao final)
print("Linha 1", end="\n\n")
print("Linha 2")
# Saída: 
# Linha 1
# 
# Linha 2

# """
# Cores:
# Para imprimir texto colorido no terminal, você pode usar sequências de escape ANSI.
# \033: É o código de escape.
# [1;31m: 1 é para negrito e 31 define a cor vermelha.
# \033[0m: Redefine o estilo ao normal para não pintar o resto do terminal.
# """
# Imprime os textos aplicando as cores correspondentes na tela do terminal
print("\033[1;31mTexto em vermelho\033[0m")
# Saída: Texto em vermelho (com a cor alterada no terminal)

print("\033[1;32mTexto em verde\033[0m")
# Saída: Texto em verde (com a cor alterada no terminal)

print("\033[1;33mTexto em amarelo\033[0m")
# Saída: Texto em amarelo (com a cor alterada no terminal)

print("\033[1;34mTexto em azul\033[0m")
# Saída: Texto em azul (com a cor alterada no terminal)

# """
# Alinhamento e Preenchimento
# """
texto = "Python"

# Reserva um espaço de 10 caracteres e empurra o texto para a esquerda
print("{:<10}".format(texto))  
# Saída: Python    

# Reserva um espaço de 10 caracteres e empurra o texto para a direita
print("{:>10}".format(texto))  
# Saída:     Python

# Reserva um espaço de 10 caracteres e centraliza o texto no meio deles
print("{:^10}".format(texto))  
# Saída:   Python   

# Centraliza o texto e preenche os espaços vazios com asteriscos
print("{:*^10}".format(texto))  
# Saída: **Python**

# """
# Exemplos Finais de Fixação:
# """
# Exemplo 1: Concatenando strings com variáveis usando a vírgula (que já adiciona um espaço automático)
var1 = 404
var2 = "SENAI"
print("Hello to the", var2, var1)
# Saída: Hello to the SENAI 404

# Exemplo 2: Usando formatação com % (modo antigo, da época do C, não recomendado para versões novas)
print("Hello to the %s %d " % (var2, var1))
# Saída: Hello to the SENAI 404

# Exemplo 3: Usando formatação com .format()
print("Hello to the {} {} ".format(var2, var1))
# Saída: Hello to the SENAI 404

# Exemplo 4: Concatenando strings usando o sinal de + e convertendo o número (int) para texto (str)
print('Hello to the ' + var2 + " " + str(var1))
# Saída: Hello to the SENAI 404

# Exemplo 5: Usando f-string (A forma mais moderna, limpa e recomendada de fazer no Python hoje!)
print(f"Hello to the {var2} {var1}")
# Saída: Hello to the SENAI 404

# Exemplo 6: Arredondamento de números injetado direto na string
pi = 3.14159
print("O valor de pi é: {:.2f}".format(pi))
# Saída: O valor de pi é: 3.14