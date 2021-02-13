def main():
    lista_tele = {}
    while True:
        mostra_menu()
        menu_escolhas = int(input("Escolha a sua opção (1-6): "))
        if menu_escolhas == 1:
            mostra_lista(lista_tele)
        elif menu_escolhas == 2:
            print("Acrescentar Nome e Número")
            nome = input("Nome: ")
            telefone = input("Número: ")
            acrescenta_numero(lista_tele, nome, telefone)
        elif menu_escolhas == 3:
            print("Retira Nome e Número")
            nome = input("Nome: ")
            retira_contacto(lista_tele, nome)
        elif menu_escolhas == 4:
            print("Procura Número")
            nome = input("Nome: ")
            print(procura_numero(lista_tele, nome))
        elif menu_escolhas == 5:
            nome_ficheiro = input("Ficheiro a carregar: ")
            carrega_lista(lista_tele, nome_ficheiro)
        elif menu_escolhas == 6:
            break
        else:
            mostra_menu()

    print("Fim")


def mostra_menu():
    print("1. Mostra Lista Telefónica")
    print("2. Acrescentar Entrada (Nome, Número)")
    print("3. Retirar Entrada (Nome, Número)")
    print("4. Procurar Número")
    print("5. Carregar Lista Telefónica")
    print("6. Terminar")
    print()


def mostra_lista(lista_tele):
        for nome, numero in sorted(lista_tele.items()):
            print()
            print('Nome: %s\nNúmero: %s' % (nome, numero))

def acrescenta_numero(lista_tele, nome, telefone):
    lista_tele[nome] = telefone
    return lista_tele


def retira_contacto(lista_tele, nome):
    if nome in lista_tele:
        del lista_tele[nome]
        return lista_tele
    else:
        print('Contacto inexistente')

def procura_numero(lista_tele, nome):
    if nome in lista_tele:
        print(lista_tele[nome])
    else:
        print('Contacto inexistente')


def carrega_lista(lista_tele, nome_ficheiro):
    with open(nome_ficheiro, 'r') as f_ent:
        for contacto in f_ent:
            dados = contacto[:-1]
            nome, numero = dados.split()
            lista_tele[nome] = numero
        return lista_tele

if __name__ == '__main__':
    main()