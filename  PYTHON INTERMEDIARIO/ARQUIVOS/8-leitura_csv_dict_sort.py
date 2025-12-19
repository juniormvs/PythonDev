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

def get_language(course):
    return course["language"]

def get_category(course):
    return course["category"]

for curso in sorted(cursos, key=get_category):
    print(f"{curso['language']} - {curso['category']}")