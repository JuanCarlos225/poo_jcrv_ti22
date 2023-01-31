

altura = float (input ('Ingresa el valor de altura: '))
base = float (input ('Ingresa el valor de base: '))
area=base*altura
perimetro=base+altura+math.sqrt(base*base+altura*altura)
print ('Valor de area: ' + repr (area))
print ('Valor de perimetro: ' + repr (perimetro))
print ()
os.system ('pause')