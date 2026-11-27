import os
import requests

# 👥 Integrantes do squad
squad = {
    "Maria": "11635-144",
    "Gustavo": "11640-714",
    "Caio": "11630-370",
    "Giacomo": "11631454"
}

# 🔎 Pesquisando uma pessoa
nome = input("🔍 Digite o nome da pessoa: ").strip().title()

if nome in squad:

    cep = squad[nome]

    # 🌐 Consultando o ViaCEP
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()

        if "erro" not in dados:
            cidade = dados["localidade"]
            estado = dados["uf"]

            print("\n👤 Nome:", nome)
            print("📮 CEP:", cep)
            print(f"📍 Cidade: {cidade} - {estado}")

        else:
            print("❌ CEP inválido!")

    else:
        print("⚠️ Erro ao consultar o ViaCEP.")

else:
    print("❌ Pessoa não encontrada no squad!")