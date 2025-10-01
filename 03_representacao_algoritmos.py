"""
Exercício 03 — Representação de Algoritmos (descrição narrativa, fluxograma e pseudocódigo)
Representação Algoritmos - Descricao fluxograma pseudocodigo

Objetivo pedagógico:
- Mostrar diferentes formas de representar um algoritmo antes de transformá-lo em código.
- Entender a importância de descrever o problema em linguagem natural, fluxograma e pseudocódigo
  antes de implementar em Python.
- Reforçar a transição entre teoria (representação) e prática (código real).

Conceitos abordados:
- Descrição narrativa.
- Fluxograma (explicação conceitual).
- Pseudocódigo.
- Implementação final em Python.

Enunciado:
1) Explique em texto (narrativa) o algoritmo para calcular a área de um retângulo.
2) Mostre como ficaria esse algoritmo em um fluxograma (explicado em texto, pois não estamos
   desenhando figuras neste exercício).
3) Escreva o pseudocódigo desse mesmo algoritmo.
4) Por fim, implemente o código em Python.

Observações didáticas:
- O objetivo aqui não é apenas "rodar um código", mas entender o caminho de representação
  até chegar no código real.
"""

# =========================
# DESCRIÇÃO NARRATIVA
# =========================
# "O algoritmo deve ler a base e a altura de um retângulo, multiplicar os dois valores
# e exibir o resultado como a área do retângulo."

# =========================
# FLUXOGRAMA (explicação em texto)
# =========================
# Início → Ler base → Ler altura → Calcular área = base * altura → Mostrar área → Fim

# =========================
# PSEUDOCÓDIGO
# =========================
# Início
#    Leia base
#    Leia altura
#    area ← base * altura
#    Escreva "A área é: ", area
# Fim

# =========================
# IMPLEMENTAÇÃO EM PYTHON
# =========================

# Entrada
base = 5  # valor fixo apenas para exemplo
altura = 3  # valor fixo apenas para exemplo

# Processamento
area = base * altura

# Saída
print("A área do retângulo é:", area)

# =========================
# COMENTÁRIO FINAL
# =========================
# Perceba como o mesmo algoritmo passou por:
# - Descrição em palavras (linguagem natural).
# - Fluxograma (visualização em blocos).
# - Pseudocódigo (estrutura próxima da programação).
# - Implementação em Python (linguagem real).
# Essa transição é fundamental no aprendizado de algoritmos.
