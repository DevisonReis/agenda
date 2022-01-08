import sqlite3

conexao = sqlite3.connect('agenda.db')
cursor = conexao.cursor()

def adicionar_contato():
    nome_contato = input('Nome do contato: ')
    numero_tel = input('Numero do contato: ')

    cursor.execute('INSERT INTO contatos (nome, numero) VALUES (?, ?)', (nome_contato, numero_tel))

    conexao.commit()

def mostrar_contatos():
    cursor.execute('SELECT * FROM contatos;')
    for contato in cursor.fetchall():
        print(contato)

def pega_nome():
    return input('Digite um nome: ')

def editar_contato():
    pesquisa = pega_nome()
    novo_nome = input('Novo nome: ')
    novo_numero = input('Novo numero: ')

    cursor.execute('UPDATE contatos SET nome = ?, numero = ? WHERE nome = ?', (novo_nome, novo_numero, pesquisa,))

    conexao.commit()

def excluir_contato():
    nome = pega_nome()
    cursor.execute('DELETE FROM contatos WHERE nome = ?', (nome,))
    conexao.commit()

def valida_opcao(pergunta, inicio, fim):
    while True:
        try:
            valor = int(input(f'{pergunta}'))
            if inicio <= valor <= fim:
                return valor
        except ValueError:
            print(f'Opção inválida, escolha um numero entre {inicio} e {fim}')

def menu():
    print('=' * 30)
    print('AGENDA DE CONTATOS')
    print('=' * 30)
    print('1 - Adicionar contato')
    print('2 - Editar contato')
    print('3 - Apagar contato')
    print('4 - Mostra contatos')
    print('0 - Sair')
    print('=' * 30)

    return valida_opcao('Escolha uma opção: ', 0, 4)

while True:
    opcao = menu()

    if opcao == 0:
        conexao.close()
        break
    elif opcao == 1:
        adicionar_contato()
    elif opcao == 2:
        editar_contato()
    elif opcao == 3:
        excluir_contato()
    elif opcao == 4:
        mostrar_contatos()
