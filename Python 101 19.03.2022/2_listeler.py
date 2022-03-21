#listeler
cars = ['Bmw','Mercedes','Opel','Mazda']
print(len(cars))
print('ilk eleman : ',cars[0],'\nSon Eleman : ',cars[-1])
cars[3] = "Toyota"
cars[-2:] = ['toyota','renault']
print(cars) 
yeniListe = cars +['audi','Nissan']
print(yeniListe)