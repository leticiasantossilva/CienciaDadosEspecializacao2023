# Plano de Codificação e Testes

## Introdução

Para desenvolver o projeto de aplicativo de análise de dados, utilizaremos a linguagem Python para codificação, uma vez que a mesma mostra-se a mais adequada ao desenvolvimento ágil de aplicações de pequena escala com interface de linha de comando.

Empregaremos REPL (Read-Eval-Print Loop) Driven Development (RDD) como método de codificação, pois integra a codificação  aos testes unitários de modo a propiciar a redução de erros de programação ao mesmo tempo em que facilita o trabalho de exploração sobre os dados, que é essencial em ciência de dados.


## Linguagem e bibliotecas

A linguagem escolhida para a programação será a linguagem Python em virtude de sua especial adequação ao trabalho com ciência de dados bem como suas capacidades como linguagem de uso geral.

Acrescenta-se a ela o uso da biblioteca Python NumPy para fornecer os arrays que serão necessários para a estimação do modelo e a biblioteca Python StatsModels para execução da regressão.


## Módulo de Entrada e Saída

### Entrada de dados

- Requisitos RU1 e RU2 - preços de fechamento
Função leitor_precos() -> array
Esta função realiza a leitura de preços de ações.

- Requisito RU3 
Função leitor_taxa() -> array
Esta função executa a leitura da taxa CDI.

- Requisito RU4

Função leitor_indice() -> array
Esta função lê o valor do índice da carteira de mercado (IBOVESPA).

Função leitor_pasta() -> string
Esta função executa a leitura do teclado para escolha da pasta de gravação na primeira iniciação do sistema.

Função leitor_acoes() -> lista
Esta função deve realizar a leitura das ações para estimação do CAPM.

### Saída de dados

- Requisito RU10
Função grava_csv(var: objetoArquivo) -> Null
Esta função produz um arquivo CSV contendo a data do resultado da estimação em cada semana em que o modelo for estimado.
 

## Módulo de Processamento

- Requisito RU5 - método de estimação do modelo
Função estima_modelo()
Esta é a função de estimação do modelo por mínimos quadrados ordinários.
 
- Requisito RU6 e RU7  - teste de nulidade do alfa de Jensen e do risco específico
Função testa_nulidade_t_parametro()
Esta função realiza teste da nulidade do alfa de Jensen (o emprego do teste t).

- Requisito RU8 - teste do modelo
Função testa_nulidade_F_parametros()
Esta função avalia a nulidade conjunta dos parâmetros da regressão (usando o teste F).

- Requisito RU9 - correlação serial 
Função testa_corr()
Esta função testa a correlação serial do modelo (usando o correlograma).
