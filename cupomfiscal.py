produtos = {123: 'Camisa estampada',
            124: 'Camisa social manga longa',
            125: 'Calça jeans'}

vendas = [(123, 3, 25.55),
          (124, 2, 79.99),
          (128, 1, 99.99)]

item = 0
valor_total = 0
print('-' * 46)
print('C U P O M F I S C A L'.center(46, ' '))
print("ITEM CÓDIGO DESCRIÇÃO QTD.UN.VL_UNIT(R$) ST VL")
print('-' * 46)


def venda(args):
    pass


for indice in range(0, len(venda)):
    subtotal = 0
    item += 1
    produto = produtos.get(venda[indice][0])
    quantidade = venda [indice][1]
    valor = venda [indice][2]
    subtotal += quantidade * valor
    valor_total += subtotal

print(f'{str(item).ljust(4)}')}
        {venda [indice] [0]}
        {produto.rjust(37)}')'