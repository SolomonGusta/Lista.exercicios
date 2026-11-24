'''
Uma escola está organizando sua primeira olimpíada do conhecimento e deseja separar os 100 alunos em dois grupos de 50. Além de testar os conhecimentos dos alunos, querem estimular a formação de novos laços sociais e, por isso, a divisão dos grupos de alunos será feita seguindo um critério:

Alunos com número de matrícula par, ficarão no grupo azul.
Alunos com número de matrícula ímpar, ficarão no grupo amarelo. 
Os alunos ainda não sabem dessa regra de separação dos grupos e, no dia do evento, quando digitarem o número da matrícula na catraca, deve aparecer no painel a cor do grupo que ele deve integrar. 

DESAFIO: Desenvolvam uma função para retornar se o número passado pelo usuario no console é par ou ímpar.

Caso o número de matrícula do(a) aluno(a) seja par imprima:
VOCÊ ESTÁ NO TIME AZUL

Caso o número de matrícula do(a) aluno(a) seja impar imprima:
VOCÊ ESTÁ NO TIME AMARELO


'''
def verificar_time(matricula):
    return (
        "🔵 VOCÊ ESTÁ NO TIME AZUL 🔵"
        if matricula % 2 == 0
        else "🟡 VOCÊ ESTÁ NO TIME AMARELO 🟡"
    )


matricula = int(input("Digite sua matrícula: "))
print(verificar_time(matricula))

def verificar_time(matricula):
    return (
        f"🔵 Matrícula {matricula}: VOCÊ ESTÁ NO TIME AZUL 🔵"
        if matricula % 2 == 0
        else f"🟡 Matrícula {matricula}: VOCÊ ESTÁ NO TIME AMARELO 🟡"
    )


matriculas = []

# Validador que permite inserir até ocupar 5 espaços (índices 0 a 4)
while len(matriculas) < 5:
    numero = int(input(f"🔢 Digite a {len(matriculas) + 1}ª matrícula: "))
    matriculas.append(numero)

print("\n📋 Resultado da divisão dos times:")

# Laço de repetição para passar todos os números da lista na função
for matricula in matriculas:
    print(verificar_time(matricula))
