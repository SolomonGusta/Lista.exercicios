from faker import Faker
import random
import pandas as pd

fake = Faker("pt_BR")
personas = []

def gerar_cpf_valido():
    # Gera os 9 primeiros dígitos
    numeros = [random.randint(0, 9) for _ in range(9)]

    # Calcula o primeiro dígito verificador
    soma = sum(n * peso for n, peso in zip(numeros, range(10, 1, -1)))
    resto = soma % 11
    digito1 = 0 if resto < 2 else 11 - resto

    # Calcula o segundo dígito verificador
    numeros.append(digito1)
    soma = sum(n * peso for n, peso in zip(numeros, range(11, 1, -1)))
    resto = soma % 11
    digito2 = 0 if resto < 2 else 11 - resto

    numeros.append(digito2)

    cpf = "".join(map(str, numeros))
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

quantidade = int(input("Quantas personas deseja criar? "))

# Gera as personas
for i in range(quantidade):
    genero = random.choice(["M", "F"])

    if genero == "M":
        nome = fake.name_male()
        emoji_genero = "👨"
    else:
        nome = fake.name_female()
        emoji_genero = "👩"

    persona = {
        "Nome": f"{emoji_genero} {nome}",
        "CPF de teste": gerar_cpf_valido(),
        "Idade": random.randint(18, 60),
        "Cidade": f"📍 {fake.city()}"
    }

    personas.append(persona)

# Cria a tabela e ordena alfabeticamente pelo nome
df = pd.DataFrame(personas)

df["Nome_ordenacao"] = df["Nome"].str.replace(
    r"^[^\w]+", "", regex=True
).str.strip()

df = df.sort_values(
    by="Nome_ordenacao",
    key=lambda coluna: coluna.str.lower()
).drop(columns="Nome_ordenacao").reset_index(drop=True)

# Exibe o resultado
print("\nPERSONAS FICTÍCIAS EM ORDEM ALFABÉTICA (A-Z)")
print("=" * 90)
print(df.to_string(index=False))
print("=" * 90)
print(f"Total de personas: {len(df)}")

# Salva o resultado no arquivo
with open("personas.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("PERSONAS FICTÍCIAS — CPFs APENAS PARA TESTE\n")
    arquivo.write("=" * 90 + "\n")
    arquivo.write(df.to_string(index=False))
    arquivo.write("\n" + "=" * 90 + "\n")
    arquivo.write(f"Total de personas: {len(df)}\n")

print("\nArquivo personas.txt criado com sucesso!")