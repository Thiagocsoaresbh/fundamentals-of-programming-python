"""
Exercício 10 — Sistema de Notas Completo

Subtítulo:
Uso de if / elif / else para múltiplas condições

Objetivo pedagógico:
- Consolidar tudo que foi visto até agora.
- Introduzir o elif (else if) para múltiplos cenários de decisão.
- Criar um programa interativo que classifique a situação do aluno com base em notas.
- Mostrar que expressões lógicas podem ser encadeadas.

Conceitos abordados:
- Estruturas condicionais compostas (if / elif / else).
- Comparações lógicas encadeadas.
- Entrada com input() e conversão para float.
- Saída com f-strings e condições múltiplas.

Enunciado:
1) Solicite ao usuário duas notas.
2) Calcule a média aritmética.
3) Se a média for maior ou igual a 7.0 → "APROVADO".
4) Se a média for entre 5.0 e 6.9 → "RECUPERAÇÃO".
5) Se a média for menor que 5.0 → "REPROVADO".
6) Exiba notas, média e situação.

Observações didáticas:
- Este exercício fecha o ciclo de entrada → processamento → saída.
- Mostra como criar condições múltiplas em programas reais.
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
    # ESTRUTURA CONDICIONAL (if / elif / else)
    # =========================
    if media >= 7.0:
        situacao = "APROVADO"
    elif media >= 5.0:
        situacao = "RECUPERAÇÃO"
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
# - O elif permite tratar múltiplos cenários sem precisar aninhar vários ifs.
# - A ordem das condições importa: Python testa de cima para baixo.
# - Este exercício integra:
#   * Entrada com input()
#   * Conversão de tipos
#   * Operadores aritméticos e relacionais
#   * Estrutura condicional
#   * Saída formatada
#
# Com este programa, fechamos o primeiro ciclo de exercícios incrementais.
# A partir daqui, podemos avançar para estruturas de repetição (for, while),
# coleções (listas, tuplas), funções e modularização.
