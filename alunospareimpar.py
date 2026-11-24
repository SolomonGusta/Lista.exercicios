def verificar_time(matricula):
    return (
        "VOCÊ ESTÁ NO TIME AZUL"
        if matricula % 2 == 0
        else "VOCÊ ESTÁ NO TIME AMARELO"
    )


matricula = int(input("Digite sua matrícula: "))
print(verificar_time(matricula))
