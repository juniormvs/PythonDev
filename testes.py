"""
palavra = "Python"
numero = 3

concatena = f"Python{palavra}"

print(concatena)
print(palavra*3)



num1 = 5
num2 = 7
num3 = 2
numeros = [num1,num2,num3]

print(numeros)
print(numeros[0])
print(sum(numeros))



cidades = ("Recife", "Salvador", "Fortaleza")
print(cidades)

print(cidades[-1])
print(len(cidades))

----------------sets-----------------
numerosSet = {4,7,4,9,7}
print(numerosSet)
print(len(numerosSet))
print(max(numerosSet))


#Criar um set vazio.
bandas_rock = set
print(type(bandas_rock))

"""

produtos = {
    "Arroz": 15.50,
    "Feijão": 8.90,
    "Macarrão": 6.75

}

print(produtos)

produtoMaisCaro = max(produtos, key=produtos.get)
print(produtoMaisCaro)
MediaPreco = sum(produtos.values()) / len(produtos)
#formatar com duas casas decimais

print(f"{MediaPreco:.2f}")