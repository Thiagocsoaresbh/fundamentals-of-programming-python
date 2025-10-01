"""
Exercício 07 — Operadores em Python

Subtítulo:
Operadores aritméticos, relacionais e lógicos com exemplos práticos

Objetivo pedagógico:
- Demonstrar os três principais grupos de operadores usados em algoritmos.
- Aplicar operadores em exemplos simples para fixar os conceitos.
- Mostrar na prática como Python resolve cada operação e retorna os resultados.

Conceitos abordados:
- Operadores aritméticos: +, -, *, /, %, **, //
- Operadores relacionais: ==, !=, >, <, >=, <=
- Operadores lógicos: and, or, not
- Importância das expressões lógicas em condições (serão usadas em if, while, etc).

Enunciado:
1) Crie exemplos para cada tipo de operador em Python.
2) Explique o que cada linha faz e o resultado esperado.
3) Mostre como combinações de operadores podem formar expressões mais complexas.
"""

# =========================
# OPERADORES ARITMÉTICOS
# =========================

a = 10
b = 3

print("Aritméticos:")
print("a + b =", a + b)   # soma: 10 + 3 = 13
print("a - b =", a - b)   # subtração: 10 - 3 = 7
print("a * b =", a * b)   # multiplicação: 10 * 3 = 30
print("a / b =", a / b)   # divisão real: 10 / 3 = 3.333...
print("a // b =", a // b) # divisão inteira (descarta casas decimais): 10 // 3 = 3
print("a % b =", a % b)   # módulo (resto da divisão): 10 % 3 = 1
print("a ** b =", a ** b) # exponenciação: 10³ = 1000

# =========================
# OPERADORES RELACIONAIS
# =========================

x = 5
y = 7

print("\nRelacionais:")
print("x == y:", x == y)   # igualdade → False
print("x != y:", x != y)   # diferente → True
print("x > y:", x > y)     # maior → False
print("x < y:", x < y)     # menor → True
print("x >= y:", x >= y)   # maior ou igual → False
print("x <= y:", x <= y)   # menor ou igual → True

# =========================
# OPERADORES LÓGICOS
# =========================

idade = 20
tem_cnh = True

print("\nLógicos:")
print("idade >= 18 and tem_cnh:", idade >= 18 and tem_cnh)  # True e True → True
print("idade >= 21 or tem_cnh:", idade >= 21 or tem_cnh)    # False ou True → True
print("not tem_cnh:", not tem_cnh)                          # negação de True → False

# =========================
# EXPRESSÃO MAIS COMPLEXA
# =========================

# Exemplo: um jovem só pode dirigir se tiver 18 anos ou mais E possuir CNH.
pode_dirigir = (idade >= 18) and tem_cnh
print("\nPode dirigir?", pode_dirigir)

# =========================
# COMENTÁRIOS FINAIS
# =========================
# - Operadores aritméticos são usados em cálculos.
# - Operadores relacionais comparam valores e retornam True/False.
# - Operadores lógicos combinam condições (booleanos).
# - O resultado de uma expressão lógica será fundamental no uso de estruturas
#   de decisão (if/else) e de repetição (while/for), que veremos em breve.
