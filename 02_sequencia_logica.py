"""
Exercício 02 — Sequência Lógica de Passos (ordem correta de execução)
Sequência Lógica de Passos - Ordem correta de execucao

Objetivo pedagógico:
- Reforçar a ideia de que um algoritmo segue uma ordem lógica e que alterar essa ordem
  pode gerar resultados incorretos.
- Mostrar como a execução de operações passo a passo afeta o resultado final.

Conceitos abordados:
- Sequência lógica de instruções.
- Importância da ordem das operações.
- Estrutura Entrada → Processamento → Saída aplicada a um exemplo simples.

Enunciado:
1) Mostre um algoritmo que calcule o preço final de um produto com desconto.
2) Os passos corretos são:
   a) Definir o preço original.
   b) Definir a porcentagem de desconto.
   c) Calcular o valor do desconto.
   d) Subtrair o desconto do preço original.
   e) Mostrar o resultado.
3) Ilustre o que acontece se inverter a ordem de alguns passos (comentado).
"""

# =========================
# ENTRADA (dados fixos)
# =========================

# Preço original do produto
preco_original = 100.0  # em reais (float)

# Porcentagem de desconto (10%)
desconto_percentual = 10.0

# =========================
# PROCESSAMENTO (cálculo correto)
# =========================

# Primeiro, calculamos o valor absoluto do desconto.
# Para isso, multiplicamos o preço pela porcentagem e dividimos por 100.
valor_desconto = (preco_original * desconto_percentual) / 100

# Depois, subtraímos o valor do desconto do preço original.
preco_final = preco_original - valor_desconto

# =========================
# SAÍDA (resultado correto)
# =========================

print("Preço original:", preco_original)
print("Desconto aplicado:", desconto_percentual, "%")
print("Valor do desconto:", valor_desconto)
print("Preço final após desconto:", preco_final)

# =========================
# EXEMPLO DIDÁTICO: ORDEM ERRADA
# =========================

# Se, por engano, subtrairmos 10 diretamente antes de calcular o desconto,
# teremos um resultado completamente incorreto.
# (Esse trecho é apenas ilustrativo, não deve ser usado como solução correta).
preco_errado = preco_original - desconto_percentual
print("\n[Exemplo incorreto] Preço final se subtrairmos direto o percentual:", preco_errado)

# Comentário: Isso mostra que seguir a sequência lógica é essencial para
# chegar ao resultado certo em algoritmos.
