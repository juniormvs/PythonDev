"""
ARQUIVOS - MODOS DE OPERAÇÃO:

1-> Modo w -write
2-> Modo a - append
3-> Modo r - read
"""

with open("dados/namesx.txt", "r", encoding="utf-8") as file:
    #print(file.read())
    for line in file:
        print(f"Olá, {line.rstrip()}")