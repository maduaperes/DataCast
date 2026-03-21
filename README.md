# DataCast

**Meu espaço para explorar e praticar tipos de dados e conversão de valores em Python.**

---

## Sobre este repositório

Este é meu laboratório pessoal, onde eu exploro e pratico conceitos de **valores primitivos em Python**, suas **representações** e como **converter entre diferentes tipos de dados**.

Aqui eu trabalho com:  
- Números: **Decimal, Binário, Octal, Hexadecimal**  
- Strings e conversão entre números e texto  
- Conversão de tipos em Python: `int()`, `float()`, `str()`, etc.  
- Concatenar variáveis e texto em `print()`  
- Operações básicas com entrada do usuário  

---

## Exemplos

```python
# Convertendo entre tipos
num = 3
num_float = float(num)   # Converte inteiro 3 para float 3.0
num_str = str(num)       # Converte inteiro 3 para string "3"

# Print com concatenação
nome = input("Digite seu nome: ")
print("Olá " + nome + "! Bem-vindo(a) ao Python!")

# Operações com input
valor_unit = float(input("Informe o valor unitário: "))
quantidade = int(input("Informe a quantidade: "))
print("O valor total é:", valor_unit * quantidade)
