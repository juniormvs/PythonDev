num1 = int(input("Digite o primeiro número: \n"))
num2 = int(input("Digite o segundo número: \n"))        


#ARTIMÉTICOS
sum = num1 + num2
sub  = num1 - num2
div = num1 / num2
mult = num1 * num2
mod = num1 % num2  
exp = num1 ** num2

print(f"Potência do número {num1} por {num2}")
print(f"Resto da divisão de {num1} por {num2}")


#Comparação
bigger = num1 > num2
smaller = num1 < num2
equal = num1 == num2
different = num1 != num2
bigger_equal = num1 >= num2
smaller_equal = num1 <= num2

print(f"Os números {num1} e {num2} são iguais? {equal}")
print(f"O número {num1} é maior ou igual a {num2}? {bigger_equal}")
print(f"O número {num1} é menor que {num2}? {smaller}")
print(f"O número {num1} é diferente de {num2}? {different}")

#Atribuição
num1 += 1  #num1 = num1 + 1
num1 -= 1  #num2 = num2 - 1
num1 *= 1  #num1 = num1 * 1
num1 /= 1  #num2 = num2 / 1
