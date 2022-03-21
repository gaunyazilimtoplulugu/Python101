#int str float boolen
sayi1 = 12 # integer 
sayi2 = 1.5 # float
sayi3 = 15 #integer
sayi4 = 24.25 #float


# toplu yorum satırı yapmak için seçer control+k+c
# toplu olarak yorumdan çıkarmak için seçeriz sonra control+k+u


# String'ler
karakter1 = "hello world" 
karakter2 = 'hello world'
karakter3 = """hello world"""
karakter4 = " hakan'ın Python dersi"
karakter5 = """hakan "ders başladı" dedi """
karakter6 = "16" # bu da string bir değerdir
#her hangi bi satırı kopyalayıp aşağıya yapıştırabilmek için shift+alt+ok tuşları
karakter7 = "16.6" # bu da string bir değerdir
# boolen'lar
durum1 = True
durum2 = False


# değişken dönüşümü
# integer to string
int_str = str(sayi1) 

# string to integer
str_int = int(karakter6)

# string to float
str_float = float(karakter7)
#type(str_int) değişkenin türünü öğrenmek için type methodu kullanılır
#print(type(str_int)) 
#print(type(str_float))

# string to string
str_str = karakter1 + karakter4
print(str_str)

# bool to integer
a = True
bool_to_int = int(a)
print(bool_to_int)

toplama = sayi1 + sayi3 + 5 
cikarma = sayi2 - sayi3 
carpma = sayi1 * sayi3
bolme = sayi2 / sayi3
bolme2 = sayi2 // sayi3 # iki tane bölme işareti koyarak küsüratı almamış oluruz
mod = 20 % 6 #bölümden kalan değeri döndürür
us = 2 ** 6 #üs alma
#print(us)

