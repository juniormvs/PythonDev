movieName = "Top Gun"

movieDescription = """O filme Top Gun Maverick, 
                            é um filme de aviação e aventura
                              muito consagrado 
                              na 
                        indústria cinematográfica."""

print(movieName.upper()) # Tudo em maiúsculo
print(movieName.lower()) # Tudo em minúsculo

print(movieName.capitalize()) # Primeira letra maiúscula
print(movieName.title()) # Primeira letra de cada palavra maiúscula
print(movieName.center(20,'-')) # Centraliza a string em um campo de 10 caracteres, preenchendo com '-'
#Resultado -Top Gun--
print(movieName.find("un")) # Retorna o índice ou posição da primeira ocorrência da substring
print(movieDescription.find("a")) # Conta quantas vezes a letra 'a' aparece na string
print(movieName.replace("Gun", "Matrix")) # Substitui uma substring por outra
print(movieDescription.split(', ')) # Divide a string em uma lista, usando a vírgula como separador
print("-".join(movieName)) # Junta os caracteres da string com '-' entre eles
print(movieName.startswith("Top")) # Verifica se a string começa com a substring especificada
print(movieName.endswith("Gun")) # Verifica se a string termina com a substring especificada
print(movieName.count("o")) # Conta quantas vezes a letra 'o' aparece na string
print(movieDescription.strip()) # Remove espaços em branco no início e no final da string
print(movieDescription.lstrip()) # Remove espaços em branco no início da string
print(movieDescription.rstrip()) # Remove espaços em branco no final da string
print(len(movieName)) # Retorna o comprimento da string
print(len(movieDescription)) # Retorna o comprimento da string
