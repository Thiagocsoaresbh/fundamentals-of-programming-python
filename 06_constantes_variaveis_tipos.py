"""
Exercício 06 — Constantes, Variáveis e Tipos de Dados

Subtítulo:
Constantes, variáveis, função type() e conversão de tipos (casting)

Objetivo pedagógico:
- Diferenciar variáveis de constantes.
- Mostrar que em Python não existe constante "nativa", mas usamos convenção (nomes em MAIÚSCULAS).
- Usar a função type() para verificar o tipo de dados.
- Mostrar conversão de tipos (int → float → str → bool).
- Entender que variáveis podem mudar de valor, enquanto constantes NÃO devem ser alteradas.

Conceitos abordados:
- Variáveis e mutabilidade.
- Constantes (convenção).
- Tipos básicos: int, float, str, bool.
- Conversão de tipos (casting).
- Função type() para inspecionar tipos.

Enunciado:
1) Crie uma constante chamada PI com valor 3.1415 (em maiúsculas, por convenção).
2) Crie variáveis de cada tipo (int, float, str, bool).
3) Mostre o valor e o tipo de cada uma usando type().
4) Faça conversões entre tipos e exiba os resultados.
"""

# =========================
# CONSTANTE (por convenção)
# =========================

# Em Python, constantes não são "protegidas". Por convenção usamos MAIÚSCULAS.
PI = 3.1415

# =========================
# VARIÁVEIS (tipos básicos)
# =========================

# Variável inteira (int)
idade = 25

# Variável real (float)
altura = 1.75

# Variável de texto (str)
nome = "Thiago"

# Variável booleana (bool)
ativo = True

# =========================
# SAÍDA DOS TIPOS
# =========================

print("Constante PI:", PI, "| Tipo:", type(PI))
print("Idade:", idade, "| Tipo:", type(idade))
print("Altura:", altura, "| Tipo:", type(altura))
print("Nome:", nome, "| Tipo:", type(nome))
print("Ativo:", ativo, "| Tipo:", type(ativo))

# =========================
# CONVERSÕES DE TIPOS (casting)
# =========================

# int → float
idade_float = float(idade)
print("\nIdade como float:", idade_float, "| Tipo:", type(idade_float))

# float → int (perde a parte decimal)
altura_inteira = int(altura)
print("Altura como int:", altura_inteira, "| Tipo:", type(altura_inteira))

# int → str
idade_str = str(idade)
print("Idade como string:", idade_str, "| Tipo:", type(idade_str))

# str numérica → int
numero_texto = "50"
numero_convertido = int(numero_texto)
print("Texto convertido em int:", numero_convertido, "| Tipo:", type(numero_convertido))

# bool → int
ativo_int = int(ativo)  # True = 1, False = 0
print("Ativo como int:", ativo_int, "| Tipo:", type(ativo_int))

# int → bool
zero_bool = bool(0)   # 0 vira False
um_bool = bool(1)     # 1 vira True
print("0 como bool:", zero_bool)
print("1 como bool:", um_bool)

# =========================
# COMENTÁRIOS FINAIS
# =========================
# - Variáveis podem mudar de valor durante o programa.
# - Constantes NÃO devem mudar (mesmo que Python permita, é convenção respeitar).
# - A função type() ajuda a inspecionar os tipos.
# - Conversões (casting) são essenciais para trabalhar com input(), que sempre retorna str.
#
# No próximo exercício (07), vamos focar em operadores (aritméticos, relacionais e lógicos).
