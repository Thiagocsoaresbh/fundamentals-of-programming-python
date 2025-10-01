"""

Tópico 1 – Fundamentos de lógica e algoritmos

Exercício 01 — Conceito de Algoritmo (introdução prática, sem entrada do usuário)
Conceito de Algoritmo - Primeiro programa com sequencia de passos

Objetivo pedagógico:
- Entender, de forma concreta, o que é um algoritmo: uma sequência finita de passos
  claros e ordenados que levam à solução de um problema.
- Visualizar a estrutura Entrada → Processamento → Saída, ainda sem interações.

Conceitos abordados:
- Algoritmo (definição, finitude, ordenação de passos e determinismo).
- Sequência lógica simples.
- Estrutura de um programa (em nível conceitual).

Enunciado:
1) Explique, em alto nível, o que é um algoritmo (neste bloco de texto).
2) Mostre uma solução mínima em Python que resolva um problema simples de forma
   sequencial (sem pedir nada ao usuário).
3) O problema será: calcular a média de três notas já definidas no código e imprimir
   o resultado com uma frase explicativa.
4) Mantenha a execução 100% determinística (mesmos dados de entrada implicam
   mesma saída).

Observações didáticas:
- Usamos valores fixos para focar no "conceito de algoritmo" e na sequência de passos.
- Em exercícios seguintes, evoluiremos para entrada do usuário, conversões de tipo,
  operadores, etc.
"""

# =========================
# ENTRADA (dados fixos)
# =========================

# Definimos três notas diretamente no código (valores de exemplo).
# Esses valores são a "entrada" do algoritmo.
nota1 = 7.5  # primeira nota (float)
nota2 = 8.0  # segunda nota (float)
nota3 = 6.5  # terceira nota (float)

# =========================
# PROCESSAMENTO (cálculo)
# =========================

# Somamos as três notas para obter a soma total.
soma = nota1 + nota2 + nota3  # operação aritmética básica de adição

# Calculamos a média dividindo a soma pelo número de elementos (3).
media = soma / 3  # operação de divisão para obter a média aritmética

# =========================
# SAÍDA (exibição do resultado)
# =========================

# Imprimimos um texto explicativo seguido do valor da média calculada.
# O print é a forma mais simples de "saída" no console.
print("A média das três notas é:", media)

# Também podemos mostrar os valores usados para reforçar a rastreabilidade.
print("Notas utilizadas:", nota1, nota2, nota3)

# =========================
# COMENTÁRIOS FINAIS
# =========================
# Este programa ilustra o conceito de algoritmo:
# 1) É finito (executa e termina rapidamente).
# 2) É claro e ordenado (Entrada → Processamento → Saída).
# 3) É determinístico (com as mesmas notas, a média será sempre a mesma).
# Em exercícios futuros, trocaremos "entradas fixas" por entradas fornecidas
# pelo usuário e ampliaremos os conceitos (variáveis, tipos, operadores, etc.).
