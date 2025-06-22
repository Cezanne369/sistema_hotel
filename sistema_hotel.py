#type:ignore
"""
Uma pousada deseja um sistema simples para gerenciar as reservas dos hóspedes. Seu objetivo é criar um programa em Python que permita ao recepcionista:

1️⃣ Adicionar uma nova reserva (Nome do hóspede, número do quarto e número de diárias). "ok'
2️⃣ Atualizar uma reserva (Modificar o número de diárias para um hóspede). ok
3️⃣ Cancelar uma reserva (Remover um hóspede do sistema). ok
4️⃣ Exibir todas as reservas ativas (Listar os hóspedes, seus quartos e diárias).ok
5️⃣ Calcular o total a pagar para um hóspede específico (Valor = diárias × preço por diária).ok

Regras do Sistema
✅ O hotel tem 20 quartos numerados de 1 a 20.
✅ O preço por diária é R$ 150,00.
✅ Se um hóspede já tiver uma reserva, não pode ser cadastrado novamente.

"""
import os

#reserva dicionario
reservas = {
    "Hóspede 1" : {'nome':'Jean','quarto': 20, 'diaria': 5 },
    "Hóspede 2": {'nome':'Gabriel', 'quarto': 10, 'diaria': 6 },
    "Hóspede 3" : {'nome':'Domênica', 'quarto': 15, 'diaria': 1 },
}

#Opção de escolha 
while True:
    print('\n======Escolha uma das opções abaixo======\n')
    print('1 - Adicionar uma nova reserva!')
    print('2 - Atualizar um cadastro')
    print('3 - Cancelar uma reserva')
    print('4 - Exibir reservas ativas')
    print('5 - Total de reservas (R$)')
    print('6 - Sair do programa')
    
    escolha = input('\nescolha uma das opções acima: ')

    #Sair do programa
    if escolha == '6':
        print('\nSaindo do programa')
        break

    #aparte de add hóspede
    if escolha == '1':
        os.system('cls')
        nome = input('Digite o seu nome: ')
        quarto = int(input('Digite um número de quarto entre (1-20): '))
        diaria = int(input('Digite a diária: '))

    #verificação de caso de reserva do mesmo hóspede
    if nome in reservas:
        print(f'O hóspede {nome} já tem uma reserva!')

    #verificação de caso de reserva do mesmo quarto, any = faz a verificação dentro da dic para ver se o quarto esta ocupado.
    elif any(reserva['quarto'] == quarto for reserva in reservas.values()):
        print(f'O quarto {quarto} já tem hóspede. Por favor, selecione outro.')

    elif quarto < 1 or quarto > 20:
        print('Por favor selecione um quarto entre 1 a 20.')
                
    else:
        # formatado desse jeito para que a informação possa entrar dentro do dicionario
        reservas[nome]= {'nome': nome ,'quarto': quarto, 'diaria': diaria} 
        print(f'\nO hóspede {nome}, foi cadastrado no apartamento nº {quarto} com uma diária de {diaria} dia')

    #parte de Atualização de cadastro       
    if escolha == '2':
        os.system('cls')
        nome = input('\nDigite o nome do cadastro que queria atualizar: ')

        if nome in reservas:
            quarto_new = int(input('\nDigite o novo número de quarto: '))
            diaria_new = int(input('\nDigite a nova diária: '))
            reservas[nome]["quarto"] = quarto_new
            reservas[nome]["diaria"] = diaria_new
            print(f'\nAtualização feita com sucesso o hóspede {nome}, esta cadastrado no quarto nº {quarto_new}, e sua diaria foi alterada para {diaria_new}')
        else:
            print('Este hóspede nao foi encontrado!')

    #parte de exclusão de cadastro
    if escolha == '3':
        os.system('cls')
        nome = input('Escolha qual cadastro deseja excluir: ')

        if nome in reservas:
            hospede_remo = reservas.pop(nome) 
            print(f'O cadastro do hóspede {nome}, foi excluido!')
        else:
            print('Este hóspede nao foi encontrado!')       

    #parte de revisar a lista de hóspedes no momento.
    if escolha == '4':
        os.system('cls')
        for chave , valor in reservas.items():
            print(f'\nHóspede: {valor["nome"]}')
            print(f'Quarto: nº {valor["quarto"]}')
            print(f'Diária: {valor["diaria"]} Dia(s)')

    #função que mostra o total de valor que tem que tem a receber dos hóspedes.
    if escolha == '5':
        os.system('cls')
        preco_diaria = int(150)
        #info = pesquisar o valor mencionado dentro do dicionario
        total = sum(info['diaria'] * preco_diaria for info in reservas.values()) 
        print(f'O valor total que tem a receber é R$ {total:.2f}!') 



    # Muito Feliz por conseguir realizar esse projeto. Parabéns para mim s2.
