import random

def palavra_aleatoria(lista_palavras):
    return random.choice(lista_palavras)

def main():
    lista_palavras = ["banana", "abacaxi", "morango", "laranja", "uva"]
    palavra = palavra_aleatoria(lista_palavras)
    print("Palavra aleatória:", palavra)

if __name__ == "__main__":
    main()
