# Dictionary Sözlükler 

import xdrlib


sozluk = {}
print(type(sozluk)) # <class 'dict'> 
sehirler = ['Adana','Gaziantep']
plakalar = [1,27]
print(plakalar[sehirler.index('Gaziantep')])

plakalar = { "Adana":1,"Gaziantep":27}
# f string methodu
# print(f"Adana'nin plakası {plakalar['Adana']}  ")
# format methodunun kullanımı
# print("Plakalar {1} {0} ".format(plakalar['Adana'],plakalar['Gaziantep']))

users = {
    'sadik turan' : {
        'age': 35,
        'email': 'sadikturan@gmail.com'
    },
    'huseyin yagmurlu' : {
        'age' : 20,
        'role' : ['student','softwarer'],
        'instagram': 'hsynygmrl' 
    }
}

print(users['sadik turan']['age'])
print(users['huseyin yagmurlu']['role'][0])

x = input('bir kullanici adi giriniz ')
print(users[x])

x = input('bir sayi giriniz: ')
print(users['huseyin yagmurlu']['role'][int(x)])