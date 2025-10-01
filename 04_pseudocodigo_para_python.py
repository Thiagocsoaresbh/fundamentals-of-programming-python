"""
Exercício 04 — Pseudocódigo → Python (tradução direta de um algoritmo)
Pseudocódigo para Python — Tradução direta passo a passo

Objetivo pedagógico:
- Treinar a leitura e a escrita de Pseudocódigo.
- Aprender a traduzir cada instrução do Pseudocódigo para Python de forma direta.
- Reforçar variáveis, tipos numéricos e a estrutura Entrada → Processamento → Saída.

Contexto:
- Ainda NÃO usaremos entrada do usuário (input). Isso virá no Exercício 05.
- Aqui simularemos a etapa "Leia" definindo valores diretamente no código,
  para focar no mapeamento semântico Pseudocódigo → Python.

Pseudocódigo (exemplo escolhido):
Início
    Leia a, b, c
    soma   ← a + b + c
    media  ← soma / 3
    produto ← a * b * c
    Escreva "Soma:", soma
    Escreva "Média:", media
    Escreva "Produto:", produto
Fim

Enunciado:
1) Reproduza o algoritmo acima em Python, definindo a, b e c no código (sem input).
2) Calcule soma, média e produto, e exiba os resultados com mensagens claras.
3) Comente linha a linha explicando o que está sendo feito.

Observações didáticas:
- A instrução "Leia" no Pseudocódigo normalmente vira input() em Python,
  mas aqui vamos manter valores definidos no código para não misturar
  com validação de entrada ainda.
"""

# =========================
# "ENTRADA" (simulada)
# =========================

# No Pseudocódigo: Leia a, b, c
# Em Python (neste exercício): definimos diretamente valores numéricos.
# Estamos usando números reais (float) apenas para mostrar que as contas
# funcionam também com decimais.
a = 4.0  # variável 'a' recebe o valor 4.0
b = 6.0  # variável 'b' recebe o valor 6.0
c = 8.0  # variável 'c' recebe o valor 8.0

# =========================
# PROCESSAMENTO
# =========================

# No Pseudocódigo: soma ← a + b + c
# Em Python: usamos o operador + para somar as três variáveis.
soma = a + b + c  # calcula a soma dos três valores

# No Pseudocódigo: media ← soma / 3
# Em Python: dividimos a soma por 3 para obter a média aritmética.
media = soma / 3  # calcula a média aritmética simples

# No Pseudocódigo: produto ← a * b * c
# Em Python: usamos o operador * para multiplicar as três variáveis.
produto = a * b * c  # calcula o produto dos três valores

# =========================
# SAÍDA
# =========================

# No Pseudocódigo: Escreva "Soma:", soma
# Em Python: usamos print() para exibir mensagens no console.
print("Valores usados:", a, b, c)          # mostra quais valores foram utilizados
print("Soma:", soma)                        # exibe o resultado da soma
print("Média:", media)                      # exibe o resultado da média
print("Produto:", produto)                  # exibe o resultado do produto

# =========================
# COMENTÁRIOS FINAIS
# =========================
# Padrões observados na tradução Pseudocódigo → Python:
# - "Leia x"            → (aqui) x = <valor_fixo>   | (mais adiante) x = input(...)
# - "Escreva ..."       → print(...)
# - "x ← expressão"     → x = expressão
# - Operações (+, -, *, /) mantêm o mesmo significado.
# - A estrutura conceitual Entrada → Processamento → Saída permanece a mesma.
#
# Próximos passos (Exercício 05):
# - Introduzir input() para realmente "ler" valores do usuário.
# - Conversão de tipos (int, float) para evitar erros ao somar/ dividir.
