#for i in range(1, 1001):
 #   if i % 2 == 0:
  #      print(i)

#___________________________________________

#numero = int(input("Digite um numero: "))

#for i in range(1, 11):
    #resultado = numero * i
    #print(resultado)

#______________________________________________________

#frutas = ["banana", "Abacaxi", "uva"]
#alergia = "uva"

#for frutas in frutas:
    #if frutas == alergia:
      #  print("uva")


#________________________________________________________
#count = 1
#while count <=10:
  #print(count)
  #count += 1

#________________________________________________________

#x = 1
#while x != 5:
  #print(f"O valor atual de x é {x}, que ainda não é igual a 5.")
  #x += 1 #Incrementa x para evitar um loop infinito

# Solicita a entrada do usuário e padroniza o texto
email = input("Digite o seu e-mail institucional: ").strip().lower()

# Verifica se o domínio obrigatório está no texto e se há algo antes do '@'
if "@jogajuntoinstituto.org" in email and not email.startswith("@"):
    print("Sucesso: O e-mail pertence ao Instituto Joga Junto.")
else:
    print("Erro: E-mail inválido. Utilize um endereço @jogajuntoinstituto.org.")
