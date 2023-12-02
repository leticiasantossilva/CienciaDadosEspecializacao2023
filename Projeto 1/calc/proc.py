"""
Módulo Proc
Descrição: Este módulo prevê funções do projeto de Calculadora com as 4 operações básicas.
Autor: Letícia Santos
Versão: 0.0.1
Data: 29/11/2023

"""


# Definindo as funções de cada operação matemática da calcuadora


# Definindo a fução de adição
def somadora(numero1: float, numero2: float) -> float:
    """Esta função pega dois números reais e retorna a soma dos dois"""
    return numero1 + numero2


# Definindo a função para diminuição
def diminuidora(numero1: float, numero2: float) -> float:
    """Esta função pega dois números reais e retorna a subtração dos dois"""
    return numero1 - numero2

# Definindo a função para multiplicação
def mult(numero1: float, numero2: float) -> float:
    """Esta função pega dois números reais e retorna a multiplicação dos dois"""
    return numero1 * numero2

# Definindo a função para divisão
def div(numero1: float, numero2: float) -> float:
    """Esta função pega dois números reais e retorna a divisão dos dois"""
    if numero2 == 0:
        resultado = "Não existe divisão por zero."
    else:
        resultado = numero1 / numero2
    return resultado

