import random

while True:
    interface = ['''            
                --------
                |      |
                |
                |
                |
                |
                -''',
                '''
                --------
                |      |
                |      O
                |
                |
                |
                -''',
                '''
                --------
                |      |
                |      O
                |      |
                |
                |
                -''',
                '''
                --------
                |      |
                |      O
                |     \|
                |       
                |
                -''',
                '''
                --------
                |      |
                |      O
                |     \|/
                |       
                |
                -''',
                '''
                --------
                |      |
                |      O
                |     \|/
                |      |
                |
                -''',
                '''
                --------
                |      |
                |      O
                |     \|/
                |      |
                |     /
                -''']

    def sorteio():
        palavras_jogo = ['palavras de sua escolha']
        escolhido = random.choice(palavras_jogo)
        return escolhido


    class Features:
        def __init__(self, palavra):
            self.palavra = palavra
            self.palavra_errada = []
            self.palavra_certa = []


        def intro(self):
            print('-' * 42)
            print('\033[32mBem vindo ao joigo da Forca\033[m')
            print('_' * 42)
            print('Adivinhe qual a palavra correta (Assunto: assunto de sua escolha)')
            print('OBS:As primeiras letras de cada palavra serão maiúsculas(incluso caso hajam espaços no nome)')


        def guess(self, letra):
            if letra in self.palavra and letra not in self.palavra_certa:
                self.palavra_certa.append(letra)
            elif letra not in self.palavra and letra not in self.palavra_errada:
                self.palavra_errada.append(letra)
            else:
                return False
            return True


        def game_its_over(self):
            return self.player_won() or (len(self.palavra_errada) == 6)


        def player_won(self):
            if not '_' in self.esconder():
                return True
            return False


        def esconder(self):
            palavra_escondida = ''

            for letra in self.palavra:
                if letra not in self.palavra_certa:
                    palavra_escondida += '_'
                else:
                    palavra_escondida += letra
            return palavra_escondida


        def status(self):
            print(f'Forca: {interface[len(self.palavra_errada)]}')
            print(f'Palavra: {self.esconder()}')
            print('Letras erradas: ')
            for letra in self.palavra_errada:
                print(letra, end = ' ')
            print()

            print('Letras corretas: ')
            for letra in self.palavra_certa:
                print(letra, end = ' ')
            print()


    jogando = Features(sorteio())
    jogando.intro()

    while not jogando.game_its_over():
        jogando.status()
        try:
            usuario = str(input('Digite uma letra: '))[0]
        except:
            print('\033[31mERRO, por favor tente novamante.\033[m')
        else:
            jogando.guess(usuario)

    jogando.status()
    if jogando.player_won():
        print('\033[32mParabéns, você VENCEU!\033[m')
    else:
        print('\033[31mGAME OVER, você perdeu!\033[m')

    try:
        continuar = str(input('Deseja continuar [S/N]? ')).upper().split()[0]
    except:
        print('\033[31mERRO, por favor digite novamente\033[m')
    else:
        if continuar == 'N':
            break
print('\033[35mMuito obrigado por jogar, volte sempre ;)\033[m')
