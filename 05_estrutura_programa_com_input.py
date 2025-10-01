"""

Tópico 2 – Tipos de dados e variáveis

Exercício 05 — Estrutura de Programa com Entrada do Usuário (input)

Subtítulo:
Entrada → Processamento → Saída com conversão de tipos (float) e f-strings

Objetivo pedagógico:
- Introduzir a função input() e explicar que ela sempre retorna texto (str).
- Mostrar a necessidade de converter o texto para número (int/float) antes de calcular.
- Reforçar a estrutura Entrada → Processamento → Saída agora com interação do usuário.
- Usar f-strings para formatar a saída de forma clara.

Conceitos abordados:
- input(), str, float(), conversão de tipos, print(), f-strings.
- Comentários linha a linha explicando cada passo.

Enunciado:
1) Peça ao usuário duas notas (decimais) e calcule a média aritmética.
2) Mostre as notas informadas e a média resultante com duas casas decimais.
3) Faça tudo de forma sequencial e comentada.

Observações didáticas:
- Aqui NÃO faremos validação de erros (try/except). Isso aparecerá mais adiante.
- O foco é entender: input() → conversão → cálculo → print formatado.
"""

# =========================
# ENTRADA (lendo do usuário)
# =========================

# input() sempre retorna uma string (texto). Ex.: "7.5"
# Para poder somar como número, precisamos converter para float.
nota1_texto = input("Digite a primeira nota (ex.: 7.5): ")  # lê texto do teclado
nota2_texto = input("Digite a segunda nota (ex.: 8.0): ")   # lê texto do teclado

# Conversão de string para float (número real) para permitir cálculos com decimais.
# Se o usuário digitar algo que não é número, dará erro (vamos tratar isso em exercícios futuros).
nota1 = float(nota1_texto)  # converte "7.5" em 7.5
nota2 = float(nota2_texto)  # converte "8.0" em 8.0

# =========================
# PROCESSAMENTO (cálculo)
# =========================

# Calculamos a média aritmética simples: (nota1 + nota2) / 2
media = (nota1 + nota2) / 2

# =========================
# SAÍDA (exibição formatada)
# =========================

# Exibimos as duas notas e a média usando f-strings.
# :.2f formata o número com 2 casas decimais (ex.: 7.50).
print(f"\nNotas informadas: {nota1:.2f} e {nota2:.2f}")
print(f"Média aritmética: {media:.2f}")

# =========================
# COMENTÁRIOS FINAIS
# =========================
# Pontos chave deste exercício:
# - input() → SEMPRE retorna texto (str).
# - Para calcular, convertemos para número: float() ou int().
# - Estrutura clássica Entrada → Processamento → Saída agora ficou interativa.
# - f-strings ajudam a formatar e tornar a saída mais clara para o aluno/usuário.
#
# No próximo exercício, ampliaremos o uso de variáveis e constantes,
# e exploraremos mais tipos (int, float, str, bool) e a função type().
