print('\033[31m Olá Mundo!')
print('\033[31;43m Olá Mundo!')
print('\033[1;31;43m Olá Mundo!')
print('\033[31;43m Olá Mundo!\033[m')
print('\033[4;30;45m Olá Mundo!\033[m')
print('\033[30m Olá Mundo!\033[m')
print('\033[7;30m Olá Mundo!\033[m')
print('\033[0;33;44m Olá Mundo!\033[m')
print('\033[7;33;44m Olá Mundo!\033[m')

a = 3
b = 5
print('Os valores são \033[32m{} e \033[31m{}.'.format(a, b))
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m !!'.format(a, b))
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m !!'.format(a, b))

nome = 'Karen'
print('Olá! Muito prazer em te conhecer, {}{}{}!!'.format('\033[4;35m', nome, '\033[m'))

nome = 'Karen'
cores = {'limpa':'\033[m','azul':'\033[34m', 'amarelo':'\033[33m', 'pretoebranco':'\033[7;30m'}
print('Olá! Muito prazer em te conhecer, {}{}{}!!'.format(cores['amarelo'], nome, cores['limpa']))

nome = 'Karen'
cores = {'limpa':'\033[m','azul':'\033[34m', 'amarelo':'\033[33m', 'pretoebranco':'\033[7;30m'}
print('Olá! Muito prazer em te conhecer, {}{}{}!!'.format(cores['pretoebranco'], nome, cores['limpa']))