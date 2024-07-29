import numpy as np                     # Load the library


# exercício 4.1 - escrever uma função fatorial


def factorial(n):
    k = 1
    for i in range(n):
        k = k*(i+1) 
    return k

factorial(4)



# exercício 4.2 - Criar uma função binomial -> binomial_rv(n, p)

from numpy.random import uniform

def binomial_rv(n, p):
    """Gera uma variável aleatória binomial.

    Args:
        n (int): número de tentativas
        p (float): probabilidade de sucesso

    Returns:
        int: número de sucessos
    """
    sucessos = 0
    for i in range(n):
        rand_value = uniform(0, 1)
        if rand_value < p:
            sucessos += 1
    return sucessos

binomial_rv(10, 0.5)





# exercício 4.3 - criar uma função aleatória, com os seguintes passos:
# 1) a moeda deve girar 10 vezes sem viés.
# 2) se cara ocorrer k vezes ou mais consecutivas, deve-se pagar 1 real
# 3) caso contrario, paga nada

# primeiro a ideia é criar uma lista q será armazenadas cada rodada
# gerar um numero aleatório entre [0,1], se o numero for < 0.5, ele recebe 1
# caso contrario 0

    
    
def jogo_moeda(rodadas=10, sequencia=2):
    """Cria um jogo da moeda em que, caso tenha 2 resultados iguais seguidos,
    o jogador ganha 1 real por cada sequencia de 2 ou mais.

    Args:
        rodadas (int): Número de rodadas
        sequencia (int): Sequencia necessária para ganhar o real

    Returns:
        None
    """
    assert sequencia >= 2, "Deve-se ter mais que duas jogadas"
    assert rodadas >= sequencia, "Número de rodadas deve ser maior que a sequencia"
    
    resultado = []
    porquinho = 0
    contador = 0
    
    for i in range(rodadas):
        prob = uniform()
        if prob < 0.5:
            resultado.append(1)
        else:
            resultado.append(0)
        
        if i == 0:
            continue    
            
        if resultado[i] == resultado[i-1]:
            contador += 1
            if contador >= sequencia - 1:  
                porquinho += 1
        else:
            contador = 0  
                
    resultado_out = ",".join(map(str,resultado))
    return print("A sequencia foi: {} \nGanho de R${},00".format(resultado_out, porquinho))
    
jogo_moeda(10,4)


# Exercício 4.4 - Exercício Avançado
# Fazer uma sequencia de Fibonacci -> x_{t+1} = x_{t} + x_{t-1} | x_0 = 0; x_1 = 1


def fibonacci_seq(n=10):
    
    assert isinstance(n, int), "O input deve ser um número inteiro."
    
    x = [0, 1]
    for i in range(n):
        x_t1 = x[-1] + x[-2]
        x.append(x_t1)
    return x
        
fibonacci_seq(15)    

