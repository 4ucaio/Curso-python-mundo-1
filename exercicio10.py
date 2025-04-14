#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar (1dolarr = 3,27)
conta = float(input('Quantos vocè tem na carteira em R$: (EX: 1000.65)'))
print('Você pode comprar US${:.2f} dolares' .format(conta / 3.27))

