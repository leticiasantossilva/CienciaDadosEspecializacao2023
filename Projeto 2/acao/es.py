"""
Módulo Entrada e Saída
Descrição: Este módulo prevê funções de entrada e saída de dados para Aplicativo de Modelagem do Mercado de Ações na B3.
Autor: Letícia Santos
Versão: 0.0.1
Data: 30/11/2023

"""

from proc import Acao

def leitora_emissor():
    """Função para inserir a razão social da empresa emissora da ação"""
    emissor = input("Qual o nome da empresa? ")
    return emissor

def leitora_codigo():
    """Função para inserir o código da ação na B3"""
    codigo = input("Qual o código na B3? ")
    return codigo

def leitora():
    """Função recebe o nome da empresa emissora e o código da ação na B3"""
    emissor = leitora_emissor()
    codigo = leitora_codigo()
    return [emissor, codigo]

empresa = leitora()

def impressora(resultado: str):
    """Função que informará ao usuário que foi criado o objeto computacional que representa a ação"""
    print(f"A ação criada foi {resultado}.")


def impressora(resultado: str):
    """Função que informará ao usuário que foi criado o objeto computacional que representa a ação"""
    print(f"A ação criada foi {resultado}.")
    
    

def impressora(acao: Acao):
    """Função que informará ao usuário que foi criado o objeto computacional que representa a ação"""
    print(acao)
    
    