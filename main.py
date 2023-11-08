# Exercico 19


lista_numeros = [3, 7, 1, 4, 9, 2, 10, 4]

soma = 0

for numero in lista_numeros:
    soma += numero

print(f"A soma dos elementos da lista é: {soma}")


print("---------------------------------")
# Exercicio 20


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

soma_pares = 0
soma_impares = 0

for numero in numeros:
  if numero % 2 == 0:
    soma_pares += numero
  elif numero % 2 != 0:
    soma_impares += numero

print(f"A soma dos valores pares é: {soma_pares} e a soma dos valores impares é: {soma_impares}")


# fim