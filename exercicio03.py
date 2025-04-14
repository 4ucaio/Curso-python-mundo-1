#Crie um script python que leia dois numeros e tente mostrar a soma entre eles.
numero1 = int(input('Digite um numero: \n'))
numero2 = int(input('Digite o segundo numero: \n'))
soma = numero1 + numero2
print ('A soma vale',soma)
print('A soma vale {}'.format(soma))
print ('A soma entre {} e {} é {}' . format(numero1, numero2, soma))