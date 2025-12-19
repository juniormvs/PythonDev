names = []

with open("dados/namex.txt","r", encoding="utf-8") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names, reverse=True):#reverse=True retorna as entradas ordenada
    print(f"Olá, {name}")


