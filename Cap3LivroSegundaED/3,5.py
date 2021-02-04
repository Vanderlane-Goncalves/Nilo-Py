'''Calcular Uma expresção em tabela verdade '''
A = [1,10,5]
B = [2,3,1]
C = [True,False, False]
D = [False, False,True]
print('A = [1,10,5] \nB = [2,3,1] \nC = [True,False, False] \nD = [False, False,True]')

i = int(input('Digite o indice para os calculos:'))
calculoDireto = bool((A[i] > B[i]) and (C[i] or D[i]))
#calculo passo a passo
calculo1 = bool(A[i] > B[i])
calculo1_1 = bool(C[i] or D[i])
calculoFinal = bool(calculo1 and calculo1_1)

print('O resultado da Expreção A(%d) > B(%d) AND C(%s) or D(%s)' % (A[i],B[i],C[i],D[i]))
print('O resultado A(%d) > B(%d) = %s e C(%s) or D(%s) = %s' % (A[i],B[i],calculo1,C[i],D[i], calculo1_1 ))
print('Resultado final da expreção:A > B AND C or D = %s'% calculoFinal )
print('Calculo direto: %s' % calculoDireto)