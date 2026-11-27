import os
import requests

# 👥 Integrantes do squad
squad = {
    "Maria": "11635-144",
    "Gustavo": "11640-714",
    "Caio": "11630-370",
    "Giacomo": "11631454"
}

# 📁 Criando a pasta
nome_pasta = "dados_squad"
os.makedirs(nome_pasta, exist_ok=True)

# 📄 Caminho do arquivo
caminho_arquivo = os.path.join(nome_pasta, "integrantes.txt")

# 💾 Salvando os dados
with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:

    for nome, cep in squad.items():

        # 🌐 Consultando a API
        url = f"https://viacep.com.br/ws/{cep}/json/"
        resposta = requests.get(url)

        if resposta.status_code == 200:
            dados = resposta.json()

            if "erro" not in dados:
                cidade = dados["localidade"]

                linha = f"👤 Nome: {nome} | 📍 Cidade: {cidade}"

                print(linha)
                arquivo.write(linha + "\n")

            else:
                print(f"❌ CEP inválido para {nome}.")

        else:
            print(f"⚠️ Erro na requisição para {nome}.")

# 🎉 Mensagem final
print(f"\n📂 Arquivo salvo com sucesso em: {caminho_arquivo}")
print("✅ Todos os integrantes foram processados!")