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

#__________________________________________________________

#def contar_vogais(palavra):
   # vogais = "aeiouAEIOU"
    #contador = 0
    
    # Loop 'for' para percorrer cada caractere da palavra
    #for caractere in palavra:
        #if caractere in vogais:
           # contador += 1
            
    #return contador

# Solicitação de entrada ao usuário
#palavra_usuario = input("Digite uma palavra: ")

# Chamada da função e exibição do resultado
#total_vogais = contar_vogais(palavra_usuario)
#print(f"A palavra '{palavra_usuario}' possui {total_vogais} vogais.")

#_________________________________________________________________

# email = input("Digite se email: ")

#if "@jogajuntoinstituto.org" in email:
  #print (f'O email: {email} é do domínio @jogajuntoinstituto.org')
#else:
    #print(f'O email: {email} Não pertence ao domínio @jogajuntoinstituto.org')

#dado que - contexto
#Quando -ação
#então - consequencia

#Dado que o usuário digita 757575eze@jogajuntoinstituto.org
#quando executa o código
#então o sistema retorna 'O email: {email} é do domínio @jogajuntoinstituto.org'

#Dado que o usuairio digita 757575exe@gmail.com
#quando executa o código 
#então o sistema retorna 'O email: {email} Não pertence ao domínio @jogajuntoinstituto.org'

#__________________________________________________________________________________________________


palavra = input ('Digite uma palavra: ')

vogais = [ 'a', 'e', 'i', 'o', 'u']

contar = 0

for letra in palavra:
   for l in vogais:
     if l == letra:
      print (f'{letra} é uma vogal')
      contar += 1
      break

print (f'A quantidade de vogais é: {contar}')
