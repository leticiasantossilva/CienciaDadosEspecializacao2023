"""
Módulo Principal
Descrição: Este é o módulo principal do Aplicativo de Modelagem do Mercado de Ações na B3.
Autor: Letícia Santos
Versão: 0.0.1
Data: 30/11/2023

"""



# Importação dos módulos

import es
from proc import Acao


# Definindo as funções

def main():
    # Leitura de dados
    dados = es.leitora()
    
    # Instanciamento do objeto
    acao = Acao(dados[0], dados[1])
    
    # Saída de dados
    es.impressora(acao)
    
    

if __name__ == "__main__":
    main()
    