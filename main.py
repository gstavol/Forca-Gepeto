from openai import OpenAI
import os
import json
import funcoes

# Pegando a chave
while True:
    minha_key = input("Digite a sua key, por favor:\n")
    if minha_key != "":
        break

client = OpenAI(api_key=minha_key)

# Recebendo o prompt
def prompt_gpt( Idioma="portugês", Tema="aleatório", Dificuldade="média"):
    prompt = f"""Preciso que gere uma lista, para meu jogo de forca, com uma palavra e uma dica seguindo esses requisitos:
    Idioma:{Idioma} (deve ser o idioma da resposta e da dica),
    Tema:{Tema} (escolha palavras diversificadas),
    Dificuldade: {Dificuldade} (leve a dificuldade muito a sério).
    O modelo de lista que eu desejo é conforme o seguinte exemplo: ["Palavra", "Dica por extenso"]
    responda em {Idioma} apenas um elemento"""

    resposta = pergunta_gpt(prompt)
    respostacerta = funcoes.format_resposta_gpt(resposta)
    respostacerta = json.loads(respostacerta)

    return respostacerta

def pergunta_gpt(pergunta):

    prompt = [{"role": "user", "content": pergunta }]

    resposta = client.chat.completions.create(
        messages = prompt,
        model = "gpt-3.5-turbo-0125",
        max_tokens = 400,
        temperature = 0
    )

    return resposta.choices[0].message.content

def limpar_tela():
    # print()
    os.system('cls' if os.name == 'nt' else 'clear')

def play_game():
    limpar_tela()
    IDIOMA = input("Digite um idioma: ")
    TEMA = input("Digite um tema: ")
    DIFICULDADE = input("Digite a dificuldade: ")

    palavra_recebida = prompt_gpt(IDIOMA, TEMA, DIFICULDADE)
    # print("resposta do gpto",type(palavra_recebida))
    palavra_correta = palavra_recebida[0]
    word_to_guess = funcoes.limpar_palavra(palavra_recebida[0])
    # print("testar se e lista: ", word_to_guess)
    guessed_letters = []
    attempts = 6

    while attempts > 0:
        palavra_ate_agora = funcoes.display_word(word_to_guess, guessed_letters)
        if palavra_ate_agora == word_to_guess:
            limpar_tela()
            print("Parabéns! Você ganhou!, a palavra era", palavra_correta)
            break
    

        limpar_tela()
        
        print("Dica da mamãe Miku: ", palavra_recebida[1])
        print()

        
        print(funcoes.desenhar_forca(attempts))

        print("Palavra:", funcoes.display_word(word_to_guess, guessed_letters))
        print("Letras:", end=" ")
        for i in sorted(guessed_letters):
            print(i, end = " ")
        guess = funcoes.limpar_palavra(input("\nDigite uma letra: "))
        if guess != "":
            guess = guess.upper()[0]
        
        if guess in guessed_letters:
            input("Você já tentou essa letra. Pressione Enter para continuar...")
            continue

        if guess != "":
            guessed_letters.append(guess)

        if guess not in word_to_guess:
            attempts -= 1

    if attempts == 0:
        limpar_tela()
        print("Você perdeu! A palavra era:", palavra_correta)


while True:
    play_game()
    limpar_tela
    while True:
        continuar = input("Deseja continuar? (S/N)\n").upper()
        if continuar == "S" or continuar == "N":
            break
    if continuar == "N":
        break
