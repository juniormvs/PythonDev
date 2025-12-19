with open("dados/cursos.csv", "r", encoding="utf-8") as file:
    for line in file:
        """linha = line.rstrip().rsplit(",")
            print(linha[0], linha[1])"""
        linguagem, categoria = line.strip().split(",")
        print(f"{linguagem} -> {categoria}")