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

def contar_vogais(palavra):
    vogais = "aeiouAEIOU"
    contador = 0
    
    # Loop 'for' para percorrer cada caractere da palavra
    for caractere in palavra:
        if caractere in vogais:
            contador += 1
            
    return contador

# Solicitação de entrada ao usuário
palavra_usuario = input("Digite uma palavra: ")

# Chamada da função e exibição do resultado
total_vogais = contar_vogais(palavra_usuario)
print(f"A palavra '{palavra_usuario}' possui {total_vogais} vogais.")
