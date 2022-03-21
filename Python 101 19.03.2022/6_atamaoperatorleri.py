# x = 5
# y = 6
# z = 7
x,y,z = 5,6,7
# print(x,y,z)

x += 1 # x = x + 1 toplama 
x -= 1 # x = x - 1 cıkarma
x *=2 # x = x*2 carpma 
x /= 5 # x = x/5 bolme 
x %= 2 # x = x%2 kalan bulma mod alma
x = 13
x //= 5 # x = x//5 bolenin tam değeri
x **=z # x = x**z 2 üzeri 7
# print(x)

values = 23,24,25
print(values)
a,b,c = values
print(a)

degerler = 1,2,3,4,5
*v,b,n = degerler
v,*b,n = degerler
v,b,*n = degerler
print(v,b,n)