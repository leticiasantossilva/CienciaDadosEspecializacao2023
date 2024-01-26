"""
Módulo Entrada e Saída

Descrição: Este módulo prevê funções de entrada e saída de dados para o aplicativo que coleta automaticamente dados da web e estima o modelo CAPM para ações na B3.
Autor: Letícia Santos e Ronaldo Debiasi
Versão: 0.0.1
Data: 13/12/2023

"""

# Importando bibliotecas necessárias

import numpy as np
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import requests
import json
import os
import csv


# ENTRADA DE DADOS


# Leitura de retornos de preços de ações

def leitor_precos(ticker:str) -> np.array:
    """" Esta função realiza a leitura de preço de fechamento de ações nas quarta-feiras de todas as últimas 260 semanas e calcula seus retornos """
    end_date = datetime.now()
    start_date = end_date - timedelta(weeks=263)
    dado = yf.download(ticker, start=start_date, end=end_date, progress=False, interval='1d')
    data_day = dado[dado.index.weekday == 2]
    fechamento = data_day['Adj Close'].pct_change().dropna()
    return np.array(fechamento)

# Leitura de retornos da carteira de mercado (IBOVESPA)

def leitor_indice() -> np.array:
    """" Esta função realiza a leitura de fechamento do Bovespa nas quartas-feiras de todas as últimas 260 semanas e calcula seus retornos """
    end_date = datetime.now()
    start_date = end_date - timedelta(weeks=263)
    bov = yf.download("^BVSP", start=start_date, end=end_date, progress=False, interval='1d')
    retorno = bov['Adj Close'].pct_change().dropna()
    mercado = retorno[retorno.index.weekday == 2]
    return np.array(mercado)    


# Leitor da taxa livre de risco

def leitor_taxa() -> np.array:
    """" Esta função realiza a leitura da taxa CDI nas quartas-feiras de todas as últimas 260 semanas """
    # URL da API de CDI diário do Bacen
    url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.12/dados?formato=json"
    api = requests.get(url)
    
    # Leitura de dados em json
    dados = api.json()
    cdi = pd.DataFrame(dados)
    
    # Formatando e filtrando período
    cdi['data'] = pd.to_datetime(cdi['data'], format='%d/%m/%Y')
    cdi['valor'] = pd.to_numeric(cdi['valor'], errors='coerce')
    end_date = datetime.now()
    start_date = end_date - timedelta(weeks=268)
    filtro = cdi[(cdi['data'] >= start_date) & (cdi['data'] <= end_date)]
    
    # selecionando as quarta-feiras
    filtro.set_index('data', inplace=True)
    dado_cdi = filtro[filtro.index.weekday == 2]
    return np.array(dado_cdi)


# Leitor das ações

def leitor_acoes() -> list:
    """ Função de leitura de teclado do código das 10 ações escolhidas para estimação do CAPM """
    acoes = []
        
    for i in range(1, 11):
        acoes.append(input(f'Digite o ticker da ação listada na B3 que deseja avaliar {i} de 10: (ex.: VALE3.SA) '))
    
    return acoes


# Escolha de pasta para gravação de dados do CAPM

def leitor_pasta() -> str:
    """ Esta função executa a leitura do teclado para a escolha da pasta de gravação dos arquivos """
    pasta_destino = input("""Digite o caminho da pasta de gravação de arquivos: """)
    return pasta_destino



# SAÍDA DE DADOS


#Função de gravação de dados CAPM em novo arquivo .csv

def grava_csv(pasta_destino: str, resultado_capm: pd.DataFrame):
    """ Esta função cria um novo arquivo CSV com os resultados a cada estimação CAPM realizada """
    arquivo = resultado_capm
    nome_arquivo = "resultados_capm.csv"
    caminho = os.path.join(pasta_destino, nome_arquivo)
    
    arquivo.to_csv(caminho, index=False)
    print(f"Resultados salvos no arquivo {nome_arquivo}")