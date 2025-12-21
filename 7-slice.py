movieName = "Top Gun"

# String [inicio : fim] - índice começa em 0 e termina em índice final -1

#1 Buscar toda a string a partir da primeira posição
print(movieName[0:])  # Top Gun

#2 Buscar toda a string até a última posição
print(movieName[:7])  # Top Gun

#3 Buscar toda a string da terceira até a última posição
print(movieName[2:])  # p Gun


"""
String [inicio : fim] - índice começa em 0 e termina em índice final -1
passo determina o incremento. Por padrão o esse número é 1

"""

#4 Buscar toda a string de 2 em 2 caracteres
print(movieName[::2])  # De dois em dois caracteres - Resultado TpGn

#5 Buscar toda a string de 1 em 1 caracter
print(movieName[1::2]) # Somente os ímpares - Resultado o u

#6 Buscar a string de trás para frente
print(movieName[::-1])  # nuG poT

#7 Buscar a string de trás para frente de 2 em 2 caracteres
print(movieName[::-2])  # n oT

#8 Buscar a string da posição 1 até a 5 de trás para frente
print(movieName[5:1:-1])  # uG p

#9 Buscar a string da posição 5 até a 1 de trás para frente de 2 em 2 caracteres
print(movieName[5:1:-2])  # Gp

#10 Buscar a string da posição 7 até a 0 de trás para frente
print(movieName[7::-1])  # nuG poT

#11 Buscar strings de posições impares de trás para frente
print(movieName[7::-2])  # u o

#12 Buscar strings de posições pares de trás para frente
print(movieName[6::-2])  # nT

