#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua media
nota = float(input('Digite a sua nota: '))
nota2 = float(input('Digite sua outra nota: '))
media = (nota + nota2) / 2
print('a media da nota {} e {} é :\n {}' .format(nota,nota2,media))
