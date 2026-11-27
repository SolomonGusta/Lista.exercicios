import pandas as pd

# 📋 Criando a tabela
dados = {
    "Nome": ["👩 Ana", "👨 Bruno", "👨 Carlos", "👩 Maria", "👨 João", "👨 Pedro", "👨 Lucas"],
    "Idade": [25, 30, 22, 28, 35, 27, 32],
    "Cidade": ["📍 Recife", "📍 Recife", "📍 Recife", "📍 Salvador", "📍 Salvador", "📍 São Paulo", "📍 Manaus"]
}

tabela = pd.DataFrame(dados)

# 🔎 Filtrando Recife
recife = tabela[tabela["Cidade"] == "📍 Recife"]

# 🖥️ Exibindo o resultado
print("🏙️ MORADORES DE RECIFE")
print(recife)
print(f"\n👥 Total: {len(recife)} pessoas")