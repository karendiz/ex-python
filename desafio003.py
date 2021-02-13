# Desafio temperatura,
# <7 = Congelando!
# <10 = Frio!
# >26 = Ótimo!

temperatura = int(input('Olá, qual a temperatura atual? '))
if temperatura <7:
    print('Nossa esta Congelando!')
elif temperatura <10:
    print('Que Frio!')
elif temperatura >26:
    print('Ótimo!')
else:
    print('O tempo esta muito agradável, tenha um bom dia!')