"""
Módulo Principal
Descrição: Este é o módulo com a função principal que integra as fases de entrada, processamento e saída de dados do Aplicativo de Modelagem de Ação na B3.
Autor: Letícia Santos
Versão: 0.0.1
Data: 30/11/2023

"""



# Importação dos módulos

import es
from proc import Acao


# Definindo a função principal

def main():
    """Esta é a função principal que integra as fases de entrada, processamento e saída de dados"""
    # Leitura de dados
    dados = es.leitora()
    
    # Instanciamento do objeto
    acao = Acao(dados[0], dados[1])
    
    # Saída de dados
    es.impressora(acao)
    
    

if __name__ == "__main__":
    main()
    