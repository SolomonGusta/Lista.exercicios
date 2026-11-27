import pandas as pd

# 📋 Criando os dados
dados = {
    "Nome": ["👨 João", "👩 Marta", "👨 Ary", "👨 Matheus", "👩 Michele"],
    "Idade": [51, 37, 23, 24, 33]
}

# 📊 Criando a tabela
tabela = pd.DataFrame(dados)

# 🖥️ Exibindo o resultado
print("📋 Tabela de Pessoas 👥")
print(tabela)
print("✅ Fim da tabela!")