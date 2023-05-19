"""lista = ["Chicago", "Queens", "Salvador", "São Paulo"]

lista2 = [2, 3, 7, 8, 10]

lista3 = [2.0, 3.5, 6.3]

lista4 =[True, False]

lista5 = [True, "Chicago", 2.5, False, 4]

# slicing
print(lista[::]) # retorna a lista inteira
print(lista[1:]) # retorna do index que destacamos até o fim da lista
print(lista[:3]) # retorna do começo da lista até o index -1
print(lista5[1:4]) # retorna do index destacado até o index 

lista += lista2
print(lista)"""

lista1 = [2.0, 3.5, 4.7]
lista2 = [1, 5, 9, 11, 15]

print(lista1)
print(lista2)

print(len(lista1))

for i in range(len(lista1)):
    print(lista1[i])

# Funções que só podem ser utilizadas com tipos de dados numéricos

print(sum(lista1)) # somatório dos elementos do vetor
print(max(lista2)) # pega o maior elemento do vetor
print(min(lista2)) # pega o menor elemento do vetor