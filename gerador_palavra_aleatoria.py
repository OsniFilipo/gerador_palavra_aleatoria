import random  # Importa o módulo random para gerar números aleatórios

def palavra_aleatoria(lista_palavras):
    """
    Função para escolher aleatoriamente uma palavra da lista fornecida.

    Argumentos:
    - lista_palavras: Uma lista de palavras da qual será escolhida a palavra aleatória.

    Retorna:
    - Uma palavra aleatória escolhida da lista.
    """
    return random.choice(lista_palavras)  # Retorna uma palavra aleatória da lista

def main():
    """
    Função principal do programa.
    """
    lista_palavras = ["banana", "abacaxi", "morango", "laranja", "uva"]  # Lista de palavras disponíveis
    palavra = palavra_aleatoria(lista_palavras)  # Escolhe uma palavra aleatória da lista
    print("Palavra aleatória:", palavra)  # Exibe a palavra aleatória escolhida

if __name__ == "__main__":
    main()  # Chama a função principal para iniciar o programa
