"""
Módulo Principal

Descrição: Este é o módulo com a função principal que integra as fases de entrada, processamento e saída de dados do  aplicativo que coleta automaticamente dados da web e estima o modelo CAPM para ações na B3.
Autor: Letícia Santos e Ronaldo Debiasi
Versão: 0.0.1
Data: 13/12/2023

"""


# Importação dos módulos

import es
import proc


# Função principal
def main():
    """ Esta é a função que integra as fases de entrada, processamento e saída de dados  """
    
    
    
    """url = "https://dados.tce.rs.gov.br/dados/municipal/balancete-despesa/2023.csv"
    print('Lendo dados da URL: https://dados.tce.rs.gov.br/dados/municipal/balancete-despesa/2023.csv')
    leitor = es.leitor_dados(url)

    variavel = es.variavel()
    
    dados = proc.coleta_dados(leitor, variavel)

    resultados = proc.media_desv(dados)

    es.impressora(resultados)

    es.plotador(dados)

"""

# Executando a função do aplicativo
if __name__ == "__main__":
    main()
    