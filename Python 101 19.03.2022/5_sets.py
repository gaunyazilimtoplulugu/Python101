# Set 
kume = {"elma","armut","çilek"}
print(type(kume))
# set'ler indekslenemezler
# print(kume[0])
kume.add('mandalina') # eleman ekleme methodudur
kume.update(['apple','kivi','elma','armut'])
kume.discard('apple')
kume.remove('elma')
print(kume)

# listedeki yinelenen elemanları bir kere yazar
liste = [1,2,3,3,3,4,4,5,6,7,7]
liste = set(liste)
# print(liste)

kume2 = {1,2}
for i in range(5):
    kume2.add(i)
    print(kume2)