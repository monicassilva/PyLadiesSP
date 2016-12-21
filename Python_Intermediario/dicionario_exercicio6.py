Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:16:31) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Use o dicionario e imprima as chaves e os valores do
# dicionário ordenado pelas chaves.
>>> cat = {'nome': 'Filoca', 'mãe':
True, 'filhotes': 9, 'idade':
4, 'raça': 'indefinida', 'cor':
['preta', 'branca'], 'localização':
(15,20)}
>>> for c in sorted(cat.keys()):
	print(c)
	print(cat.get(c))

	
cor
['preta', 'branca']
filhotes
9
idade
4
localização
(15, 20)
mãe
True
nome
Filoca
raça
indefinida
>>> 
