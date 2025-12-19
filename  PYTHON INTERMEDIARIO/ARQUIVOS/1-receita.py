name = input("Digite o nome do aluno:\n")


"""
ARQUIVOS - MODOS DE OPERAÇÃO:

1-> Modo w -write
2-> Modo a - append
3-> Modo r - read
"""


#Implementação 1

file = open("dados/namex.txt","a", encoding="utf-8")
file.write(f"{name}\n")
file.close()


# Implementação 2
with open("dados/namesx.txt", "a", encoding="utf-8") as file:
    file.write(f"{name}\n")

