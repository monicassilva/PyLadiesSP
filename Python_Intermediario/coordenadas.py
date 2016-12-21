Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:16:31) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #Copie o arquivo dicionarios.py e renomeie para coordenadas.py.
#Altere para colocar o uso das três funções anteriormente criadas com
#o dicionário coordenadas.
>>> def mostra_chaves(d):
	for item in d.keys():
		print(item)

		
>>> def mostra_valores(d):
	for item in d.values():
		print(item)

		
>>> def mostra_chaves_valores(d):
	for k, v in d.items():
		print(k)
		print(v)
		print('---')

		
>>> coordenadas = {(1,1):'cafeteria ', (300,990): 'petshop ', (2,4): { '1 andar ': None, '2 andar ': ['restaurante ', 'bar ', 'banheiros '], '3 andar': 'estacionamento '}, (5, 100, 400000): 'topo dacolina '}
>>> mostra_chaves(coordenadas)
(5, 100, 400000)
(2, 4)
(1, 1)
(300, 990)
>>> mostra_valores(coordenadas)
topo dacolina 
{'2 andar ': ['restaurante ', 'bar ', 'banheiros '], '1 andar ': None, '3 andar': 'estacionamento '}
cafeteria 
petshop 
>>> mostra_chaves_valores(coordenadas)
(5, 100, 400000)
topo dacolina 
---
(2, 4)
{'2 andar ': ['restaurante ', 'bar ', 'banheiros '], '1 andar ': None, '3 andar': 'estacionamento '}
---
(1, 1)
cafeteria 
---
(300, 990)
petshop 
---
