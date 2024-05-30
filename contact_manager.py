import json
import os
import csv

contacts = []
path_folder = 'data'
list_contacts = 'contacts.txt'
fullpath_contacts = os.path.join(path_folder, list_contacts)

# Função de adicionar um novo contato
def add_contact():
    name = input('Informe o nome do contato: ')
    phone = int(input('Informe o telefone do contato: '))
    email = input('Informe o e-mail do contato: ')

    global contacts
    contacts.append({"nome": name, "telefone": phone, "e-mail": email})

    for idx, contact in enumerate(contacts, start=0): 
        contact["id"] = idx
        
    print('Contato adicionado com sucesso!')

# Função para visualizar os contatos
def view_contacts():
    if not contacts:
        print('Sua agenda está vazia, tente adicionar um contato!')
    else:
        print('Agenda:')
        for contact in contacts:
            print(contact)

# Função de atualizar um contato
def update_contact():
    id_contact = int(input('Digite o ID do contato que deseja atualizar:'))
    option_update = 0
    while option_update != 4:
        print('''[1] - Atualizar Nome
    [2] - Atualizar Telefone
    [3] - Atualizar E-mail
    [4] - Sair''')
        option_update = int(input('>>>>>> O que você quer atualizar? '))
        #Atualizar Nome
        if option_update == 1:
            name_update = input('Informe o novo nome do contato: ')
            print(f"Contato {contacts[id_contact]['nome']} atualizado para {name_update} com sucesso!")
            contacts[id_contact]['nome'] = name_update
        #Atualizar Telefone
        elif option_update == 2:
            phone_update = input('Informe o novo telefone do contato: ')
            print(f"Contato {contacts[id_contact]['telefone']} atualizado para {phone_update} com sucesso!")
            contacts[id_contact]['telefone'] = phone_update
        #Atualizar Email
        elif option_update == 3:
            mail_update = input('Informe o novo e-mail do contato: ')
            print(f"Contato {contacts[id_contact]['e-mail']} atualizado para {mail_update} com sucesso!")
            contacts[id_contact]['e-mail'] = mail_update
        #Voltar ao menu
        elif option == 4:
            print('Voltando...')
        #Opção inválida
        else:
            print('Opção Inválida')

# Função de remover um contato
def remove_contact():
    id_contact = int(input('Digite o ID do contato que deseja excluir:'))
    del(contacts[id_contact])
    for idx, contact in enumerate(contacts, start=0): 
        contact["id"] = idx
    print('Contato removido com sucesso!')

# Função para salvar lista de contatos
def save_contacts():
    with open(fullpath_contacts, 'w') as file:
        json.dump(contacts, file, ensure_ascii=False, indent=4)

    print(f'A lista de dicionários foi salva no arquivo {list_contacts} com sucesso!')

def open_list_contacts():
    # Abrir o arquivo em modo de leitura
    with open(fullpath_contacts, 'r') as file:
        leitor_csv = csv.reader(file)
        for linha in leitor_csv:
            contacts.append(linha)

    print('Dados lidos do arquivo:')
    print(contacts)


# Menu de Navegação
option = 0
while option != 6:
    print('''[1] - Adicionar Contato
[2] - Visualizar Agenda
[3] - Atualizar Contato
[4] - Excluir Contato
[5] - Carregar Lista de Contatos
[6] - Sair''')
    option = int(input('>>>>>> Selecione: '))
    if option == 1:
        add_contact()
    elif option == 2:
        view_contacts()
    elif option == 3:
        update_contact()
    elif option == 4:
        remove_contact()
    elif option == 5:
        open_list_contacts()
    elif option == 6:
        save_contacts()
        print('SAIR')
        
    else:
        print('Opção Inválida')
        