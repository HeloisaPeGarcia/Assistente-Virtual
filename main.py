

import wikipedia
wikipedia.set_lang("pt")

def pesquisar_wikipedia(pergunta):
    try:
        resposta = wikipedia.summary(pergunta, sentences=2)
        return resposta
    except wikipedia.exceptions.PageError:
        return "Desculpe, não encontrei informações sobre isso."
    except wikipedia.exceptions.DisambiguationError as e:
        return "Desculpe, encontrei várias opções. Por favor, seja mais específico na sua pergunta."

def main():
    print("Olá! Sou um assistente virtual integrado à Wikipedia.")
    while True:
        pergunta = input("Qual é a sua pergunta? (Digite 'sair' para encerrar) ")
        if pergunta.lower() == 'sair':
            break
        resposta = pesquisar_wikipedia(pergunta)
        print(resposta)
        

if __name__ == "__main__":
    main()
