import pprint

filmsDict ={
    "Inception": {
        "title": "Inception",
        "yearRelease": 2010,
        "imbdRating": 8.8,
        "genres": ["Action", "Thriller", "Sci-Fi"]
    },
    "The Dark Knight": {
        "title": "The Dark Knight",
        "yearRelease": 2008,
        "imbdRating": 9.0,
        "genres": ["Action", "Crime", "Drama"]
    },
    "Interstellar": {
        "title": "Interstellar",
        "yearRelease": 2014,
        "imbdRating": 8.6,
        "genres": ["Adventure", "Drama", "Sci-Fi"]
    }
}

print(filmsDict)
pp = pprint.PrettyPrinter(depth=4)
pp.pprint(filmsDict)
print(len(filmsDict))

#1 Buscar uma informação dentro de um dicionário aninhado
print(filmsDict["Inception"]["genres"])

#2 Adicionar um novo item ao dicionário
filmsDict["Inception"]["director"] = "Christopher Nolan"
print(filmsDict["Inception"])

#3 Excluir um dicionário
del filmsDict["Interstellar"]
pp.pprint(filmsDict)