# 1Faça um programa que calcule a média de três números inseridos pelo usuário.

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

media = (numero1+numero2+numero3)/3

print(f"A média dos três números são: {media:.2f}")

# 2Crie um programa que determine se um número inserido pelo usuário é par ou ímpar.

numero = int(input("Digite um número: "))
if (numero % 2 == 0):
    print("É par")
else:
    print("É ímpar")

# 3Escreva um programa que solicite um número ao usuário e imprima todos os números pares de 0 até esse número.
#numero = int(input("Digite um número: "))

for i in range(0, numero + 1, 2):
    print(i)

# 4Crie um programa que leia uma lista de números e exiba o maior e o menor valor da lista.

lista = [17, 2, 13, 32, 5, 8, 16]

lista.sort()
primeiro_elemento = lista[0]
ultimo_elemento = lista[-1]

print("Primeiro elemento: ", primeiro_elemento)
print( "Ultimo elemento: ", ultimo_elemento)

# 5Faça um programa que leia uma lista de números e retorne a média dos números pares.

lista = [17, 2, 13, 32, 5, 8, 16]
listap = []

for elemento in lista:
    if elemento % 2 == 0:
        
        listap.append(elemento)

print("Os números pares da lista são: ", listap)

if len(listap) > 0:
    media = sum(listap)/len(listap)
    print("A média dos números pares são: ", media)
else:
    print("Não há números pares.")

# 6Escreva um programa que peça um número inteiro positivo ao usuário e calcule o fatorial desse número.

numero_inteiro = int(input("Digite um número inteiro: "))
contador = numero_inteiro 
fatorial = 1

print("O fatorial de {}! é: ".format(numero_inteiro))

while contador > 0:
    print("{}".format(contador), end=" ")
    print("x" if contador > 1 else "=", end=" ")
    fatorial *= contador
    contador -= 1
print("{}".format(fatorial))

# Crie um programa que imprima a sequência de Fibonacci até um valor inserido pelo usuário.

numero = int(input("Digite um número: "))
termo1 = 0
termo2 = 1
termo3 = 0

print("{} -> {}".format(termo1,termo2), end=" ")

while termo3 <= numero:
    print("-> {}".format(termo3), end = " ")
    termo3 = termo1 + termo2
    termo1 = termo2
    termo2 = termo3

#  Faça um programa que determine se um número é primo ou não.

numero = int(input("Digite um número: "))

if numero < 2:
    print(f"{numero} não é um número primo.")
else:
    eh_primo = True
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            eh_primo = False
            break
    
    if eh_primo:
        print(f"{numero} é um número primo.")
    else:
        print(f"{numero} não é um número primo.")

# Escreva um programa que leia uma lista de nomes e retorne uma nova lista com apenas os nomes que começam com a letra 'A'.

nomes = input("Digite os nomes separados por espaço: ").split()

nomes_com_a = []
for nome in nomes:
    if nome[0].upper() == 'A':  
        nomes_com_a.append(nome)

print("Nomes que começam com a letra 'A':", nomes_com_a)

# Crie um programa que simule o jogo "Pedra, Papel e Tesoura" entre o usuário e o computador. O programa deve solicitar a escolha do usuário e, em seguida, escolher aleatoriamente a escolha do computador e determinar o vencedor.

def determinar_vencedor(escolha_usuario, escolha_computador):
    if escolha_usuario == escolha_computador:
        return "Empate!"
    elif (escolha_usuario == "pedra" and escolha_computador == "tesoura") or \
         (escolha_usuario == "tesoura" and escolha_computador == "papel") or \
         (escolha_usuario == "papel" and escolha_computador == "pedra"):
        return "Você venceu!"
    else:
        return "O computador venceu!"

def escolher_computador(vez):
    if vez == 0:
        return "pedra"
    elif vez == 1:
        return "papel"
    else:
        return "tesoura"

escolha_usuario = input("Escolha pedra, papel ou tesoura: ").lower()

vez = len(escolha_usuario) % 3
escolha_computador = escolher_computador(vez)

print(f"Você escolheu: {escolha_usuario}")
print(f"O computador escolheu: {escolha_computador}")

resultado = determinar_vencedor(escolha_usuario, escolha_computador)
print(resultado)





    



        