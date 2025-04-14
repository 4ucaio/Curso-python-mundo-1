#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele:
A = input('Digite algo: \n')
print ('o tipo primitivo desse valor é : ', type(A))
print ('É um numero? ', A.isnumeric())
print ('É um alfabetico? ', A.isalpha())
print ('É um alfanumerico? ', A.isalnum())
print ('É um espaço? ', A.isspace())
print ('Estar em minusculas? ', A.islower())
print ('Esta em maiusculas? ', A.isupper())
print ('Está capitalizada? ', A.istitle())






