def somar(a, b):
    return a + b


# Pede os dois números ao usuário
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Chama a função, guarda o resultado retornado e mostra na tela
resultado = somar(numero1, numero2)
print("A soma é:", resultado)
