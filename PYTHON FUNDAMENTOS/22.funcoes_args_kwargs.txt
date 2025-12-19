"""
*args - Utilizamos ele quando não temos certeza de quantos argumentos queremos ter numa função
- Os argumentos são passados como uma tupla
**kwargs - Além dos valores, podemos passar também as respectivas keys(chaves) para cada argumento
- Os argumentos são passados como um dicionário
"""
#1 - Soma de números
def sum(*num):#Entra em uma tupla
    sum_total = 0
    for n in num: #Faz for dentro de uma tupla
        sum_total +=n #Retorna o valor encontrado dentro da tupla e adiciona ao sum_total
    print(f"A soma total é {sum_total}")

sum(1)
sum(1,10,100,15,25)

#2 - Apresentação de Cursos
def presentation(**data):
    for key, value in data.items():
        print(f"{key} - {value}")
print("--------Lista de Cursos---------")

presentation(name="Python", category="backend", level="Iniciante")
presentation(name="Visão Computacional com Python", category="IA", level="Avançado")
presentation(name="Dashboards com Dash", category="Data Science", level="Intermediário")
