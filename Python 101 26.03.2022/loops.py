# While ve For

# while
a = 3
b = 6

# while a<b:
#     print("a b'den küçüktür.")

#     a = a+1

i = 1

# while i<6:
#     print(i)
#     i +=1 # i = i+1
#     if i == 3:
#         print("i =3")
#         continue
        
# while 1 :
#     deger  = input("A giriniz: ") # "A "

#     if deger == "A":
#         print("A girdiniz")
#         break
#     else:
#         print("Doğru değeri girmediniz. Tekrar deneyiniz")
#         continue


# For loops


tuple_meyveler = ("armut","muz","portakal")

# for x in tuple_meyveler:
#     print(x)

# for i in "elma":
#     print(i)

meyveler = ["elma","muz","portakal"]
# for i in meyveler:
    

#     if i == "muz":
#         continue

#     print(i)    
liste = []

# for i in range(0,10,3): # [0,3,6,9]
#     liste.append(i)

#     print(liste)

# else:
#     print("For döngüsü bitti")

#nested loops

sıfat = ["kırmızı","turuncu","yeşil"]

meyveler = ["elma","portakal","armut"]

for x in sıfat:
    for y in meyveler:
        print(x,y)
