
# 😊 Aqui pedimos o nome do aluno
nome = input("😊 Digite seu nome: ")

# 📝 Agora pedimos as 4 notas do aluno
# O int() transforma o que foi digitado em número inteiro
nota1 = int(input("📝 Digite a primeira nota: "))
nota2 = int(input("📝 Digite a segunda nota: "))
nota3 = int(input("📝 Digite a terceira nota: "))
nota4 = int(input("📝 Digite a quarta nota: "))

# ➕ Aqui somamos todas as notas
soma = nota1 + nota2 + nota3 + nota4

# 🧮 Aqui dividimos a soma por 4 para descobrir a média
media = soma / 4

# 📚 Agora mostramos o nome e a média do aluno
print(50 * "=")
print("🎓 RESULTADO DO ALUNO")
print(50 * "=")

print("😊 Olá,", nome)
print("📚 Sua média é:", media, "pontos!")

# 😢 Se a média for menor que 5, o aluno não passou
if media < 5:
    print("😢 Não passou! Estude mais!")

# 😅 Se a média não for menor que 5, vamos verificar se é menor que 7
else:
    if media < 7:
        print("😅 Passou raspando! Mas passou!")

    # 🔥 Se não for menor que 7, o aluno foi muito bem!
    else:
        print("🔥 Aí sim! Parabéns!")

# 🎉 Aqui encerramos nosso programa
print(50 * "=")
print("👏 Fim do exercício!")
print(50 * "=")
