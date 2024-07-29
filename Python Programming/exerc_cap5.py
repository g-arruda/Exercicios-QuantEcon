

# Exercício 5.1
# Parte 1 - Dado duas tuplas numéricas x_val e y_val,
# calcule o produto interno utilizando zip()


def inner_prod(x_val,y_val):
    result = 0
    for x,y in zip(x_val,y_val):
        prod = x*y
        result += prod
    return result


inner_prod(x_val=(5,7), y_val=(3,9))


# Parte 2 - Conte os números impares na sequencia 0,...,99 em apenas uma linha

def contador_num_impares(n):
    seq = list(range(n))
    contador = 0
    for i in seq:
        if i % 2 != 0:
            contador+=1
    return print(f'\nTem um total de {contador} números impares. \n')

contador_num_impares(100)

# Agora fazendo tudo em uma linha
contador = sum(1 for x in range(100) if x % 2 != 0)




# Parte 3 - Dado pairs = ((2, 5), (4, 2), (9, 8), (12, 10)),
# conte os pares (a,b) em que ambos são par.

pairs = ((2, 5), (4, 2), (9, 8), (12, 10))

def contando_pares(x):
    contador = 0
    for i in x:
        if i[0] % 2 == 0 and i[1] % 2 == 0:
            contador += 1
    return contador

contando_pares(pairs)


qnt_pares_par = sum(1 for x in pairs if x[0] % 2 == 0 and x[1] % 2 == 0)
print(qnt_pares_par)



# Exercício 5.2
# Criar uma função polinomial p(x, coef) -> p(x) = a_0 + a_1*x^1 + a_2*x^2 +...
# x é um numero real e coef é um vetor

def func_pol(x, coef):
    result = 0 
    for i,j in enumerate(coef):
        result += j * x**i

    return result

func_pol(1, (2,4))



# Exercício 5.3
# Criar uma função que recebe um string como argumento e conta quantas
# letras maiúsculas tem.


def count_upper(string):
    
    assert isinstance(string, str), "O argumento deve ser uma string."
    
    return sum(x.isupper() for x in string)    
    


count_upper("Abc D")


# Exercício 5.4
# Criar uma função que receba duas sequencias como argumento
# E retorna TRUE se a primeira sequencia esta contida na segunda
# NÃO USAR O MÉTODO "SET"



def esta_contida(seq_a, seq_b):
    for i in seq_a:
        if i not in seq_b:
            return False
    return True


def alt_esta_cont(seq_a, seq_b):
    return all(elemento in seq_b for elemento in seq_a)
       

a = list(range(1,10))
b = list(range(1,9))

esta_contida(b,a)

alt_esta_cont(b,a)



# Exercício 5.5.
# Criar uma função "linapprox" que faça uma interpolação linear
# A função deve receber estes argumentos:

# Uma função f() que vai mapear o intervalo [a,b] na reta real
# dois escalares a,b que dará os limites do intervalo
# Um inteiro "n" que vai determinar o numero de "grid points"






# Exercício 5.6
# usar a comprehension syntax para simplificar o loop

import numpy as np

n = 100
ϵ_values = []
for i in range(n):
    e = np.random.randn()
    ϵ_values.append(e) 

n = 100

e_values = [np.random.randn() for i in range(n)]


