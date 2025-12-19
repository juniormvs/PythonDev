movieName = "Top Gun"
movieName2 = "top Gun"

print(movieName == movieName2)  # False Case sensitive comparison

movieDescription = """O filme Top Gun Maverick é um filme de aviação e aventura muito consagrado na indústria cinematográfica."""

movieDescription = """O filme Top Gun Maverick 
                            é um filme de aviação e aventura
                              muito consagrado 
                              na 
                        indústria cinematográfica."""
print(movieName)
#1 MULTIPLICAÇÃO DE STRINGS
print("-------------------")
linha = "-"
print(linha * 70)  # Print a line of 70 dashes
print(movieDescription) # Multiline string

#2 PROCURAR UMA PALAVRA NA STRING
print("top" in movieName)  # True
print("ação" in movieDescription)  # True
print("ação" not in movieDescription)  # False
print("Aventura" in movieDescription)  # False Case sensitive
print("Aventura" not in movieDescription)  # True Case sensitive