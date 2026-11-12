nome = input("Digite o nome do cachorro: ")
idade_humana = int(input("Digite a idade humana do cachorro: "))

# 1 ano humano = 7 anos de cachorro
idade_cachorro = idade_humana * 7

# 2) Cálculo do lucro em 12 meses
porte = input("Digite o porte do cachorro (grande, medio ou pequeno): ").strip().lower()

# Valores corretos:
# grande: banho R$75,00 | custo R$20,00
# medio: banho R$60,00 | custo R$15,00
# pequeno: banho R$50,00 | custo R$5,00

banhos = int(input("Quantos banhos o cachorro tomou nos últimos 12 meses? "))

if porte == "grande":
    valor_banho = 75.00
    custo_banho = 20.00
elif porte == "medio":
    valor_banho = 60.00
    custo_banho = 15.00
elif porte == "pequeno":
    valor_banho = 50.00
    custo_banho = 5.00
else:
    print("Porte inválido! Use: grande, medio ou pequeno.")
    exit()

lucro_por_banho = valor_banho - custo_banho
lucro_total = lucro_por_banho * banhos

print(f"Olá, {nome} tem {idade_cachorro} anos e nos últimos 12 meses o lucro com este animal foi de R${lucro_total:.2f}")