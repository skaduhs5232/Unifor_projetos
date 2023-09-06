#EQUIPE: THIAGO DE OLIVEIRA, WILLIAM ALVES VIEGAS, CARLOS EDUARDO GONCALVE
p = input('Digite v ou f para o primeiro numero: ')
q = input('Digite v ou f para o segundo numero: ')
print(' Conjunção(^)')
print(' Disjunção(v)')
print(' Disjunção exclusiva(~v)')
print(' Condicional(->)')
print(' Bicondicional(<->)')
print(' Negação(~~)')
op = str(input())



if(op=="^"):
  if(p=='v' and q=='v'):
    print('O resultado deu V')
  else:
    print('O resultado deu F')
if(op=="v"):
  if(p=='v' or q=='v'):
    print('O resultado deu V')
  else:
    print('O resultado deu F')
if(op=="~v"):
  if((p=='v' and q=='f') or (p=='f' and q=='v')):
    print('O resultado deu V')
  else:
    print('O resultado deu F')
if(op=="->"):
  if(p=='v' and q=='f'):
    print('O resultado deu F')
  else:
    print('O resultado deu V')
if(op=="<->"):
  if((p=='v' and q=='v') or (p=='f' and q=='f')):
    print('O resultado deu V')
  else:
    print('O resultado deu F')

if(op=="~~"):
  if(p=='v'):
    print('O resultado deu F')
  else:
    print('O resultado deu V')

  
