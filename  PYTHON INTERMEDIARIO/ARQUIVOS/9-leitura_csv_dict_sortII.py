cursos = []

with open("dados/cursos.csv", "r", encoding="utf-8") as file:
    for line in file:
        """linha = line.rstrip().rsplit(",")
            print(linha[0], linha[1])"""
        linguagem, categoria = line.strip().split(",")
        curso = {}
        curso['language'] = linguagem
        curso['category'] = categoria
        cursos.append(curso)

print(cursos)


for curso in sorted(cursos, key=lambda course: course['language']):
    print(f"{curso['language']} - {curso['category']}")