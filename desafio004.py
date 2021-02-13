#Escrever nome do aluno
# Inserir varias notas
#escrever o nome do aluno e Fazer a media

print('{:-^40}'.format('SEJA BEM VINDO!'))
print('')
nomeAluno = str(input('Digite o nome do Aluno(a): '))
r = 0
soma = 0
qdte = 0
while r == 0:
    notas = float(input('Digite uma nota ou 0 para sair: '))
    if notas == 0:
        break
    soma += notas
    qdte +=1
media = soma/qdte
print('')
print('A média final do aluno(a) {} é de {} '.format(nomeAluno, media))
print('')
print('{:-^40}'.format('FIM DO PROGRAMA'))