import random


# Função para exibir o inventário
def mostrar_inventario(inventory):
    print('\n-- Inventário --')
    if inventory:
        for item in inventory:
            print(f'- {item}')
    else:
        print('Inventário vazio.')
    print('\n')


# Função para mostrar a saúde do jogador
def mostrar_saude(saude):
    print(f'Saúde: {saude}/100')


# Função para explorar a cabana
def explorar_cabana(inventory, saude):
    print('\nVocê está na cabana.')
    print('A cabana tem uma espada e uma poção de cura!')
    escolha = int(input('1. Pegar espada e poção.\n2. Voltar.\nEscolha: '))

    if escolha == 1:
        inventory.extend(['Espada', 'Poção de cura'])
        print('\nVocê pegou a espada e a poção de cura!\n')
        explorar_segundo_comodo(inventory, saude)
    else:
        print('Você escolheu sair da cabana.')


# Função para explorar o segundo cômodo da cabana
def explorar_segundo_comodo(inventory):
    print('Você encontrou um arco na estante!')
    escolha = int(input('1. Pegar o arco.\n2. Voltar.\nEscolha: '))

    if escolha == 1:
        inventory.extend(['Arco', '5x Flechas', 'Livro encantado'])
        print('\nVocê pegou o arco, flechas e um livro encantado!\n')
        escolha = int(input('1. Olhar inventário.\n2. Voltar.\nEscolha: '))

        if escolha == 1:
            mostrar_inventario(inventory)
            print('\nParabéns!!!\nVocê completou o jogo!\n')
        else:
            print('\nParece que você está com medo de abrir a mochila... Game Over!\n')
    else:
        print('Parece que você ficou com medo de entrar no segundo cômodo...')


# Função para explorar a floresta
def explorar_floresta(inventory, saude):
    print('\nVocê entrou na floresta escura.')
    escolha = int(input('1. Acionar lanterna.\n2. Voltar.\nEscolha: '))

    if escolha == 1:
        print('Oh não! Um monstro apareceu!\n')

        if 'Espada' in inventory or 'Arco' in inventory:
            combate = int(input('1. Lutar.\n2. Fugir.\nEscolha: '))

            if combate == 1:
                if 'Espada' in inventory:
                    print('Você usou a espada e derrotou o monstro!')
                elif 'Arco' in inventory:
                    print('Você usou o arco e flechas para derrotar o monstro!')
                saude -= random.randint(5, 20)  # Monstro causa dano
            else:
                print('Você fugiu com segurança.')
        else:
            print('Você não tem armas e o monstro atacou você!')
            saude -= random.randint(20, 40)  # Dano alto por falta de armas
    else:
        print('Parece que você ficou com medo de entrar na floresta.')

    return saude


# Função para usar itens do inventário
def usar_item(inventory, saude):
    if 'Poção de cura' in inventory:
        print('Você usou uma poção de cura e restaurou 20 de saúde!')
        saude += 20
        inventory.remove('Poção de cura')
    else:
        print('Você não tem uma poção de cura.')

    return saude


# Função principal do jogo
def iniciar_jogo():
    print('---- WELCOME ----\n')
    username = input('Escolha seu nome de usuário: ')
    saude = 100
    inventory = []

    while True:
        mostrar_saude(saude)
        game = int(input('\n1. Iniciar jogo.\n0. Sair.\nEscolha: '))

        if game == 1:
            print('\n1. Ir para a cabana.\n2. Entrar na floresta.\n3. Ver inventário.\n4. Usar item de cura.\n')
            escolha = int(input('Sua escolha: '))

            if escolha == 1:
                explorar_cabana(inventory, saude)
            elif escolha == 2:
                saude = explorar_floresta(inventory, saude)
                if saude <= 0:
                    print('Você foi derrotado. Game Over!')
                    break
            elif escolha == 3:
                mostrar_inventario(inventory)
            elif escolha == 4:
                saude = usar_item(inventory, saude)
            else:
                print('Escolha inválida. Tente novamente.')
        else:
            print('\nDesligando o sistema!\n')
            break


# Executa o jogo
iniciar_jogo()
