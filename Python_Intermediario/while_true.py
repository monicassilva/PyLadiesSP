# Soma de números inteiros até ser digitado zero

soma =0
while True:
   x=int(input('Digite o numero: '))
   if x ==0:
       break
     soma= soma +x
print('Soma: %d' %soma)



