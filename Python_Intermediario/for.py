#Dada a lista linguagens = ['Java', 'JavaScript','PHP', 'C', 'Python'], verifique
#apenas linguagens que comecem com a letra P e imprima na tela com letras maiúsculas.

linguagens = ['Java', 'JavaScript',
'PHP', 'C', 'Python']

for n in linguagens:
    if n.startswith ('P'):
        print (n.upper())
