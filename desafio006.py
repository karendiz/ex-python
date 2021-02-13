def main():
    lista_tele = {}
    while True:
        mostra_menu()
        menu_escolhas = int(input("Seja Bem Vindo! Escolha uma opção (1-5): ".center(62)))
        if menu_escolhas == 1:
            print("Incluir")
            nome = input("Nome: ")
            telefone = input("Número: ")
            incluir_numero(lista_tele, nome, telefone)
        elif menu_escolhas == 2:
            print("Pesquisar Número")
            nome = input("Nome: ")
            print(pesquisar_numero(lista_tele, nome))
        elif menu_escolhas == 3:
            print("Excluir Número")
            nome = input("Nome: ")
            excluir_contato(lista_tele, nome)
        elif menu_escolhas == 4:
            imprimir(lista_tele)
        elif menu_escolhas == 5:
            break
        else:
            mostra_menu()

    print("Saiu!")


def mostra_menu():
    print('-' * 62)
    print('CATÁLOGO TELEFÔNICO'.center(62, ' '))
    print("""
   1 - Incluir Contato
   2 - Pesquisar contato
   3 - Excluir contato
   4 - Imprimir Catálogo
   5 - Sair
""")
    print('-' * 62)


def incluir_numero(lista_tele, nome, telefone):
    lista_tele[nome] = telefone
    return lista_tele


def excluir_contato(lista_tele, nome):
    if nome in lista_tele:
        del lista_tele[nome]
        return lista_tele
    else:
        print('O contato não existe')

def pesquisar_numero(lista_tele, nome):
    if nome in lista_tele:
        print(lista_tele[nome])
    else:
        print('O contato não existe')

def imprimir(lista_tele):
        for nome, numero in (lista_tele.items()):
            print()
            print('Nome: %s\nNúmero: %s' % (nome, numero))


if __name__ == '__main__':
    main()