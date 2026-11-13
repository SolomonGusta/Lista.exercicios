
# 🐶 Aqui pedimos o nome do cachorro
nome = input("🐾 Digite o nome do cachorro: ")

# 🎂 Aqui perguntamos a idade do cachorro em anos humanos
idade_humana = int(input("🎂 Digite a idade humana do cachorro: "))

# 🐕 Aqui multiplicamos a idade por 7 para fazer a conversão
idade_cachorro = idade_humana * 7

# 📏 Aqui perguntamos o tamanho do cachorro
# strip() tira os espaços extras e lower() deixa tudo em letras minúsculas
porte = input("📏 Digite o porte do cachorro (grande, medio ou pequeno): ").strip().lower()

# 🛁 Aqui perguntamos quantos banhos ele tomou durante o ano
banhos = int(input("🛁 Quantos banhos o cachorro tomou nos últimos 12 meses? "))

# 💰 Aqui verificamos o tamanho do cachorro para saber o preço do banho
if porte == "grande":
    valor_banho = 75.00  # Preço cobrado pelo banho
    custo_banho = 20.00  # Quanto custa para o pet shop fazer o banho

elif porte == "medio":
    valor_banho = 60.00
    custo_banho = 15.00

elif porte == "pequeno":
    valor_banho = 50.00
    custo_banho = 5.00

else:
    # ❌ Se digitar um porte diferente, mostramos uma mensagem de erro
    print("❌ Porte inválido! Use: grande, medio ou pequeno.")
    exit()

# 💵 Aqui calculamos quanto sobra de cada banho
lucro_por_banho = valor_banho - custo_banho

# 🧮 Aqui multiplicamos o lucro de cada banho pela quantidade de banhos
lucro_total = lucro_por_banho * banhos

# 🎉 Agora mostramos o resultado final na tela
print(50 * "=")
print("🐶 RESULTADO DO PET SHOP")
print(50 * "=")

print(f"🐾 Olá! {nome} tem {idade_cachorro} anos.")
print(f"🛁 Quantidade de banhos: {banhos}")
print(f"💰 O lucro total com este animal foi de R${lucro_total:.2f}")

print(50 * "=")
print("❤️ Obrigado pela preferência!")
print(50 * "=")
