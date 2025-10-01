"""
3- Estruturas de controle

Exercício 09 — Mini Sistema de Notas com Condições

Subtítulo:
Entrada → Processamento → Saída + Estrutura Condicional (if/else)

Objetivo pedagógico:
- Reforçar a estrutura básica de um programa interativo.
- Introduzir a decisão condicional (if/else) aplicada a um problema real.
- Usar entrada validada (try/except) e operadores relacionais/lógicos.
- Mostrar como mensagens claras tornam o programa didático.

Conceitos abordados:
- Entrada de dados com input()
- Conversão para float
- Estrutura condicional if/else
- Comparações lógicas (>=, <)
- Mensagens explicativas

Enunciado:
1) Solicite ao usuário duas notas.
2) Calcule a média aritmética.
3) Se a média for maior ou igual a 7.0 → aluno aprovado.
4) Caso contrário → aluno reprovado.
5) Exiba as notas, a média e a situação do aluno.

Observações didáticas:
- Este exercício conecta tudo que vimos: entrada, tipos, operadores e if/else.
- É o primeiro passo para pensar em programas que tomam decisões.
"""

# =========================
# ENTRADA COM VALIDAÇÃO
# =========================

try:
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))

    # =========================
    # PROCESSAMENTO
    # =========================
    media = (nota1 + nota2) / 2

    # =========================
    # ESTRUTURA CONDICIONAL
    # =========================
    if media >= 7.0:
        situacao = "APROVADO"
    else:
        situacao = "REPROVADO"

    # =========================
    # SAÍDA
    # =========================
    print(f"\nNotas informadas: {nota1:.2f}, {nota2:.2f}")
    print(f"Média: {media:.2f}")
    print(f"Situação do aluno: {situacao}")

except ValueError:
    print("\nERRO: Digite apenas números válidos (use ponto para decimais).")

# =========================
# COMENTÁRIOS FINAIS
# =========================
# - A estrutura if/else é essencial para qualquer programa que precisa tomar decisões.
# - A condição (media >= 7.0) é uma expressão lógica que retorna True ou False.
# - Este é um exemplo real de aplicação prática em lógica de programação.
# - No próximo exercício (10), vamos ampliar este sistema,
#   adicionando mais condições (aprovado, recuperação, reprovado).
