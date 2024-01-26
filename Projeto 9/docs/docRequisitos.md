# CAPModeler - Documento de Requisitos

## Introdução 

Este documento apresenta os requisitos para o projeto de desenvolvimento de um aplicativo de ciência de dados em economia e finanças.

### Problema

O cliente solicitou um aplicativo que colete automaticamente dados da web e estime o modelo CAPM para ações na B3, tendo como saída o beta da ação, o alfa Jensen e a volatilidade estimada do retorno do ativo.

## Definição do Sistema

O sistema deverá coletar dados de preço de fechamento das quarta-feiras de todas as semanas durante 260 semanas (5 anos), a amostra deverá conter dados de 10 empresas com ações negociadas no mercado à vista da B3. Deverá ser calculado o beta das ações, bem como o alfa de Jensen e risco específico (volatilidade estimada do resíduo do CAPM) das ações; acrescentando o resultado em um arquivo CSV denominado `resultados_capm.csv` para cada semana.

## Especificação de requisitos do sistema

### Requisitos de usuário

#### Requisito RU1 - coleta de dados
A coleta de dados deve ser feita no site do Yahoo Finance.

#### Requisito RU2 - preços de fechamento
Os preços de fechamento das ações negociadas deverão ser coletados.

#### Requisito RU3 - ativo livre de risco
O ativo livre de risco será a taxa CDI.

#### Requisito RU4 - carteira de mercado
A carteira de mercado será o Índice Ibovespa.

#### Requisito RU5 - método de estimação do modelo
O modelo deverá ser estimado por mínimo quadrados ordinários.

#### Requisito RU6 - teste do alfa de Jenses
O alfa de Jensen deverá ser testado para nulidade com o emprego do teste t.

#### Requisito RU7 - risco específico
O risco específico de cada ação deverá ser testado também com teste t.

#### Requisito RU8 - teste de modelo
Deverá ser realizado o teste F para avaliar nulidade conjunta dos coeficientes da regressão do CAPM.

#### Requisito RU9 - correlação serial
Deverá ser testada a correlação serial do modelo, usando o correlograma.

#### Requisito RU10 - arquivo de saída
O arquivo de saída deverá conter a data do resultado da estimação em cada semana em que o modelo for estimado.


### Requisitos de Sistema

#### Requisito RSIS1 - arquivo de saída
O arquivo de saída csv deverá conter a data do resultado da estimação em cada semana em que o modelo for estimado como uma tabela para cada ação do seguinte tipo:

Data, Alfa, Beta, Sigma.

## Especificação de requisitos de Software

## Requisito RSOF1 -

Coleta automatizada de dados.

## Requisito RSOF2 -

Gravação do arquivo em uma pasta definida pelo usuário.
