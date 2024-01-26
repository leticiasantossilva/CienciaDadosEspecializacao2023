# Documento de Projeto de Software

Autor: Letícia Santos e Ronaldo Debiasi
Data: 13/12/2023

## Introdução
Este documento reúne as etapas referentes ao projeto de desenvolvimento do aplicativo de ciência de dados em economia e finanças:


## Projeto de arquitetura

A aplicação deverá ter os seguintes módulos:

### Módulo de entrada e saída - es.py
Este módulo oferecerá as seguintes funções:

#### Requisitos RU1 e RU2 - preços de fechamento
Função de leitura de preços de ações - leitor_precos()

#### Requisito RU3 
Função de leitura da taxa CDI - leitor_taxa()

#### Requisito RU4 e Requisito RU10
- Função para ler o valor do índice da carteira de mercado (IBOVESPA) - leitor_indice()
- Função de leitura do teclado para escolha da pasta de gravação na primeira iniciação do sistema - leitor_pasta()
- Função de leitura das ações para estimação do CAPM - leitor_acoes()
- Função de escrita que produz um arquivo CSV contendo a data do resultado da estimação em cada semana em que o modelo for estimado - grava_csv()
 

### Módulo de inferência econométrica do CAPM - proc.py
Este módulo oferecerá funções para estimar os seguintes parâmetros solicitados:

#### Requisito RU5 - método de estimação do modelo
Função de estimação do modelo por mínimos quadrados ordinários - estima_modelo()
 
#### Requisito RU6 e RU7  - teste de nulidade do alfa de Jensen e do risco específico
Função que realiza teste da nulidade do alfa de Jensen (o emprego do teste t) - testa_nulidade_t_parametro()

#### Requisito RU8 - teste do modelo
Função que avalia a nulidade conjunta dos parâmetros da regressão (usando o teste F) - testa_nulidade_F_parametros()


#### Requisito RU9 - correlação serial 
Função que testa a correlação serial do modelo (usando o correlograma) - testa_corr()


## Projeto de estruturas de dados

- Os códigos B3 das ações deverão ser guardados em listas.
- A pasta de gravação deverá ser guardada em um string.
- Os preços das ações deverão ser guardados em um array.


## Projeto de algoritmos

Aqui colocoremos apenas as assinaturas das ações, deixando ao desenvolvedor a escolha do algoritmo ótimo.

- leitor_pasta() -> string
- leitor_acoes() -> lista
- leitor_precos() -> array
- grava_arquivo(var: objetoArquivo) -> Null

