#faça um programa que leia um numero inteiro e mostre na tela o seu sucessor e seu antecessor
n = int(input('Digite um numero: \n'))
antecessor = n - 1 
sucessor = n  + 1
print ('O sucessor do numero {} é : {} \n o antecessor é: {}' .format(n,sucessor,antecessor))
