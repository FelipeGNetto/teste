n1 = int(input("Valor 1 de 5: "))
n2 = int(input("Valor 2 de 5: "))
n3 = int(input("Valor 3 de 5: "))
n4 = int(input("Valor 4 de 5: "))
n5 = int(input("Valor 5 de 5: "))

if n1 > n2 and n1 > n3 and n1 > n4 and n1 > n5:
    print("O primeiro número é o maior")
elif n2 > n1 and n2 > n3 and n2 > n4 and n2 > n5:
    print("O segundo número é o maior")
elif n3 > n1 and n3 > n2 and n3 > n4 and n3 > n5:
    print("O terceiro número é o maior")
elif n4 > n1 and n4 > n2 and n4 > n3 and n4 > n5:
    print("O quarto número é o maior")
elif n5 > n1 and n5 > n2 and n5 > n3 and n5 > n4:
    print("O quinto número é o maior")

