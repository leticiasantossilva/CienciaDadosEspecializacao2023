"""
Módulo de Processamento
Descrição: Este módulo prevê funções de processamento de dados para Aplicativo de Modelagem do Mercado de Ações na B3.
Autor: Letícia Santos
Versão: 0.0.1
Data: 30/11/2023

"""



class Acao:
    def __init__(self, emissor, codigo_b3):
        """Método inicializador da classe Acao"""
        self.emissor = emissor
        self.codigo_b3 = codigo_b3
    def __str__(self):
        """Método que instancia objeto da classe Acao"""
        return f"""Este é um objeto da classe Ação. O emissor da ação é {self.emissor} e o código é {self.codigo_b3}"""
    def negociar(self):
        """Prevê uma futura função da classe Acao, que ainda não foi implementado"""
        print("Não implementado")
        NotImplemented
        
        