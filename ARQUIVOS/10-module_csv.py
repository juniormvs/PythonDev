import csv

cursos = []

with open("dados/cursos.csv","r", encoding="utf-8") as file:
    #Imprime o objeto, dicionário no caso
    """reader = csv.DictReader(file)
        print(reader)"""
    
    #Imprime o dicionário
    """reader = csv.DictReader(file)
        for row in reader:
            print(row)"""
    
    # Imprime os nomes dos campos
    """reader = csv.DictReader(file)
    print(reader.fieldnames)    """

    # Imprime todo o arquivo cursos.csv e traz em forma de dicionário, contendo as keys e os valores, 'language' 'category' respectivamente
    reader = csv.DictReader(file)
    for row in reader:
        cursos.append({
            "language":row["language"],
            "category":row["category"]
        })

    

print(cursos)