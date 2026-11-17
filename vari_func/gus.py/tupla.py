
# 1. Criar uma tupla com 5 raças de cachorros
dados = ("Labrador", "Poodle", "Bulldog", "Beagle", "Golden Retriever")

# 2. Alterar a tupla para uma lista
lista = list(dados)

# 3. Inserir 2 raças extras na lista usando append()
lista.append("Pastor Alemão")
lista.append("Rottweiler")

# Inserir mais raças usando extend()
lista.extend(["Husky Siberiano", "Shih Tzu"])

# 4. Remover o primeiro dado da lista
lista.pop(0)

# 5. Remover o último dado da lista
lista.pop()

print("======================================== EXECUÇÃO DO TESTE ======================================== ")

# 6. Imprimir o primeiro dado da lista
print("🐶 Primeira raça:", lista[0])

print(50*"==")

# 7. Imprimir a quantidade de dados da lista
print("📊 Quantidade de raças:", len(lista))

print(50*"==")

# 8. Criar um dicionário
cachorro = {
    "Nome": "Golden Retriever",
    "Idade": 5,
    "Profissão": "Cão de companhia"
}

# 9. Imprimir somente o valor da chave Nome
print("🐕 Nome da raça:", cachorro["Nome"])

print(50*"==")

# Mostrar todas as raças
print("🐾 Lista completa de raças:", lista)

print(50*"==")

# Mensagem final
print("✅ Código executado com sucesso!")

print(50*"==")
