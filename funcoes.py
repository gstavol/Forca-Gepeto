import regex
import unicodedata

# Gera a palavra incompleta
def display_word(word, guessed_letters):
    displayed_word = ''
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        elif letter == " ":
            displayed_word += " "
        else:
            displayed_word += '_'
    return displayed_word


# Formatando a resposta
def format_resposta_gpt(resposta):
    posiçao = resposta.find("[")
    return resposta[posiçao:]


# Tratamento das palavras
def desacentuar(palavra):
    normalizado = unicodedata.normalize('NFD', palavra)
    return regex.sub(r'[\u0300-\u036f]', '', normalizado)

def limpar_palavra(palavra):
    palavra = desacentuar(palavra)
    return regex.sub(r'[^\p{L} ]', '', palavra).upper()

# Desenhar a forca
def desenhar_forca(tentativas_erradas):
    estagios = [  
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
          ---
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
          ---
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
          ---
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
          ---
        ''',
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |     
          ---
        ''',
        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
          ---
        ''',
        '''
           --------
           |      |
           |      
           |    
           |      
           |     
          ---
        '''
    ]
    return estagios[tentativas_erradas]