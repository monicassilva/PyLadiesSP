#Pratique o for com keys() e values() do seguinte dicionário:

>>> cat = {'nome': 'Filoca', 'mãe':
True, 'filhotes': 9, 'idade': 4,
'raça': 'indefinida', 'cor': ['preta',
'branca'], 'localização': (15,20)}
>>> cat
{'nome': 'Filoca', 'localização': (15, 20), 'cor': ['preta', 'branca'], 'filhotes': 9, 'idade': 4, 'mãe': True, 'raça': 'indefinida'}
>>> for chave in cat.keys():
	print (chave)

	
nome
localização
cor
filhotes
idade
mãe
raça
>>> 

>>> for valor in cat.values():
	print (valor)

	
9
True
indefinida
4
(15, 20)
['preta', 'branca']
Filoca

