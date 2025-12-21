#PythonFlix
nome = "Top Gun: Maverick"
ano = 2022
genero = "Ação"
duracao = 130  # duração em minutos
diretor = "Joseph Kosinski"
elencoPrincipal = ["Tom Cruise", "Miles Teller", "Jennifer Connelly"]
classificacao = "PG-13"
sinopse = "Após mais de trinta anos de serviço como um dos melhores aviadores da Marinha, Pete 'Maverick' Mitchell está onde pertence, desafiando os limites como um piloto de testes corajoso e destemido."
avaliacoes = [8.5, 9.0, 8.8, 9.2, 8.7]  # notas dos usuários
# Calculando a média das avaliações
mediaAvaliacoes = sum(avaliacoes) / len(avaliacoes)
planIncluded = False
print(f"Filme: {nome} ({ano})")
print((f"Filme: {nome} ({ano})"))
print(f"Gênero: {genero}")
print(f"Duração: {duracao} minutos")
print(f"Diretor: {diretor}")
print(f"Elenco Principal: {', '.join(elencoPrincipal)}")
print(f"Classificação: {classificacao}")
print(avaliacoes)
print(f"Sinopse: {sinopse}")
print(f"Média das Avaliações: {mediaAvaliacoes:.1f}/10")
print(f"Plano Incluído: {planIncluded}")

print(type(nome))
print(type(ano))
print(type(duracao))
print(type(avaliacoes))
print(type(planIncluded))
print(type(mediaAvaliacoes))
print(type(elencoPrincipal))
print(type(sinopse))
print(type(classificacao))
print(type(diretor))
print(type(genero))
print(type(avaliacoes))


