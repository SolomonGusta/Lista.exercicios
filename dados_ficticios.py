
import pandas as pd

# 📂 Ler o arquivo CSV
df = pd.read_csv("dados_ficticios (1).csv")

# 🔎 Filtro 1: Pessoas com idade maior que 40 anos
pessoas_mais_40 = df[df["idade"] > 40]

# 💰 Filtro 2: Pessoas com renda maior que R$ 5.000
pessoas_renda_5000 = df[df["renda"] > 5000]

# 💵 Filtro 3: Pessoas com renda maior que R$ 15.000
pessoas_renda_15000 = df[df["renda"] > 15000]

# 📊 Exibir os resultados
print("\n=== PESSOAS COM MAIS DE 40 ANOS ===")
print(pessoas_mais_40[["nome", "idade", "renda"]].to_string(index=False))

print("\n=== PESSOAS COM RENDA MAIOR QUE R$ 5.000 ===")
print(pessoas_renda_5000[["nome", "idade", "renda"]].to_string(index=False))

print("\n=== PESSOAS COM RENDA MAIOR QUE R$ 15.000 ===")
print(pessoas_renda_15000[["nome", "idade", "renda"]].to_string(index=False))

# 📈 Quantidade de pessoas em cada grupo
print("\n=== QUANTIDADE DE PESSOAS ===")
print(f"Mais de 40 anos: {len(pessoas_mais_40)}")
print(f"Renda maior que R$ 5.000: {len(pessoas_renda_5000)}")
print(f"Renda maior que R$ 15.000: {len(pessoas_renda_15000)}")

# 💾 Salvar os resultados em arquivos CSV
pessoas_mais_40.to_csv("pessoas_mais_40.csv", index=False)
pessoas_renda_5000.to_csv("pessoas_renda_5000.csv", index=False)
pessoas_renda_15000.to_csv("pessoas_renda_15000.csv", index=False)

print("\nArquivos CSV criados com sucesso!")
