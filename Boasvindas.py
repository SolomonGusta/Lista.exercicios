nomes = ["Ana", "Carlos", "Beatriz"]

nome_digitado = input("Digite seu nome: ")

if nome_digitado in nomes:
    print("Bem-vindo(a),", nome_digitado)
else:
    print("Nome não encontrado.")
