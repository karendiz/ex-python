nome = str(input('Olá, qual o seu nome?'))
if nome == 'Karen':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
    print('Olá,{}!'.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruIMm! ESTUDE MAIS!')

#print('PARABENS' if m >=6 else 'ESTUDE MAIS') - Assim também funcionalidiane