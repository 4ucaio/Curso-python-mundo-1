#Faça um progrmaa que leia a largura e a altura de uma parede em metros, calcule a sua area e a quantidade de tinta necessaria para pintá-la, sabendo que cada litro de tinta pinta uma area de 2m^2.
largura = float(input('Qual a largura da parede:\n'))
altura = float(input('Qual a altura da parede: \n'))
area = largura * altura
tintausada = area / 2
print(' a parede tem {}m^2 , Gastará {} Litros' .format(area,tintausada))
