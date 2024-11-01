# Aula 1 - Aplicando conceitos básicos na interface de um jogo.

# Login
print('---- WELCOME ----\n')
username = str(input('Choose your username: '))

# Determina se o jogo abrirá
game = int(input('\n1.Start Game(1).'
                 '\n2.Quit(0).\n'
                 'Choose: '))

#1.Inicializa o jogo
if game:
    inventory = []

    print('\n1.Go to your cabin.\n'
          '2.Go through the jungle.\n')

    escolha = int(input('Your choice is: '))

    # 2. 1º CÔMODO DA CABANA
    if escolha == 1:
        print('\nA cabana tem uma espada!\n'
              '1.Pegar espada.\n'
              '3.Voltar.\n')

        escolha = int(input('Your choice is: '))

        # 3. PEGANDO A ESPADA
        if escolha == 1:
            print('\nBela escolha! Pelo visto, havia uma bainha, uma pederneira e um mapa junto com a espada...\n'
                  '1.Próximo cômodo.\n'
                  '2.Voltar.\n')

            # Adiciona itens encontrados ao inventário
            inventory.append('Espada')

            # Adiciona múltiplos itens por vez
            inventory.extend(['Pederneira', 'Bainha', 'Mapa'])

            escolha = int(input('Your choice is: '))

            # 4. 2º CÔMODO DA CABANA
            if escolha == 1:
                print('\nEncontrou um arco na estante!\n'
                      '1.Pegar o arco.\n'
                      '2.Voltar\n')

                escolha = int(input('Your choice is: '))

                # 5. PEGANDO ARCO
                if escolha == 1:
                    print('\nWow! O arco veio com flechas e um livro...\n'
                          '1. Olhar inventário.\n'
                          '2.Voltar\n')

                    # Adiciona items encontrados ao inventário
                    inventory.extend(['Arco', '5x Flechas', 'Livro encantado'])

                    escolha = int(input('Your choice is: '))

                    # 6. Mostra o inventário
                    if escolha == 1:
                        print('\n-- Inventário --')

                        for item in inventory:
                            print(f'{item}')

                        print('\nCongratulations!!!\n'
                              'You ended the game!\n')
                    else:
                        print('\nParece que você está com medo de abrir a mochila...\n'
                              'Game over pra você...\n')

            # 4. FOGIU DO 2º CÔMODO DA CABANA
            else:
                print('Parece que você ficou com medo de entrar no cômodo da cabine..\n'
                      'Tente novamente medroso!\n')

        # 3. FUGIU DO 1º CÔMODO DA CABANA
        else:
            print('Parece que você ficou com medo de entrar na cabine...\n'
                  'Tente novamente medroso!\n')

    # 2. FLORESTA
    else:
        print('\nA floresta é escura!\n'
              '1.Acionar lanterna.\n'
              '3.Voltar.\n')

        escolha = int(input('Your choice is: '))

        # 3. 1º PASSO NA FLORESTA
        if escolha == 1:
            print('Oh no! Você assustou o monstro e ele te atacou...\n'
                  'Tenha cuidado na próxima tentativa.\n')

        # 3. FOGIU DA FLORESTA
        else:
            print('Parece que você ficou com medo de entrar na floresta!\n'
                  'Tente novamente medroso!\n')

#1.Encerra o jogo
else:
    print('Desligando o sistema!\n')
