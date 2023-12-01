"""
Módulo Principal
Descrição: Este módulo define a função principal da calculadora básica.
Autor: Letícia Santos
Versão: 0.0.1
Data: 29/11/2023

"""



# Importação dos módulos

import es
import proc


# Definindo as funções
def escolhedora(dados: list) -> float:
    """Esta função escolhe a operação de acordo com o usuário"""
    if dados[1] == "+":
        resultado = proc.somadora(dados[0][0], dados[0][1])
    elif dados[1] == "-":
        resultado = proc.diminuidora(dados[0][0], dados[0][1])
    elif dados[1] == "*":
        resultado = proc.mult(dados[0][0], dados[0][1])
    else:
        resultado = proc.div(dados[0][0], dados[0][1])
    return resultado


def main():
    dados = es.leitora()
    reultado = escolhedora(dados)
    es.escritora(resultado)
    
    
# Execução

if __none__ == "__main__":
    main()
    