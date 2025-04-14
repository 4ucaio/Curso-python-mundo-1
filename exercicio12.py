#Faça um algoritmo que leia o preço de um produto e mostre o seu novo preço, com 5% de desconto
preço = float(input('qual o preço do produto:    \n'))
novopreço = preço * 95/100
print(' O preço era R${} e agora com desconto: R${}' .format(preço,novopreço))
