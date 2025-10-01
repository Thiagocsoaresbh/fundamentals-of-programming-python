"""
Exercício 08 — Entrada e Saída com Validação

Subtítulo:
Input do usuário, conversão com tratamento de erros (try/except)

Objetivo pedagógico:
- Reforçar que input() sempre retorna string.
- Mostrar como tratar erros de conversão usando try/except.
- Ensinar a validar entradas numéricas básicas antes de prosseguir com cálculos.
- Demonstrar a importância de mensagens claras para o usuário.

Conceitos abordados:
- input()
- try/except (tratamento de erros)
- Validação de entrada
- Saída formatada

Enunciado:
1) Solicite ao usuário duas notas (decimais).
2) Use try/except para garantir que o valor digitado pode ser convertido em float.
3) Se a conversão for bem-sucedida, calcule e mostre a média com 2 casas decimais.
4) Se não for, mostre uma mensagem de erro amigável.
"""

# =========================
# ENTRADA COM VALIDAÇÃO
# =========================

try:
    # input() retorna texto, por isso fazemos conversão dentro de try
    nota1 = float(input("Digite a primeira nota (ex.: 7.5): "))
    nota2 = float(input("Digite a segunda nota (ex.: 8.0): "))

    # =========================
    # PROCESSAMENTO
    # =========================
    media = (nota1 + nota2) / 2

    # =========================
    # SAÍDA
    # =========================
    print(f"\nNotas informadas: {nota1:.2f} e {nota2:.2f}")
    print(f"Média aritmética: {media:.2f}")

except ValueError:
    # Captura erro de conversão (quando usuário digita texto não numérico)
    print("\nERRO: Você deve digitar apenas números (use ponto para decimais).")

# =========================
# COMENTÁRIOS FINAIS
# =========================
# - try/except evita que o programa quebre quando o usuário digita algo inválido.
# - Esse padrão é essencial em programas reais, pois o usuário pode sempre errar.
# - Aqui introduzimos a ideia de "programa robusto".
# - No próximo exercício (09), vamos criar uma validação condicional mais elaborada,
#   simulando um pequeno sistema de notas (aprovado/reprovado).
