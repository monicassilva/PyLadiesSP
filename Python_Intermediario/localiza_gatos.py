#Em um arquivo chamado localiza_gatos.py, escreva uma função chamada achei_uns_gatos que percorra o dicionário e imprima o
#nome do gato que está em uma dada coordenada. Teste a função com as coordenadas (4, 0) e (10,10)

>>> def achei_uns_gatos(coord_gatos, coord_do_local):
	for nome_do_gato, coord_do_local in coord_gatos.items():
		if coord_do_local == coord_gatos:
			print (nome_do_gato)

>>> coord_gatos = {'pompom': (1,1), 'Mingau': (4,0), 'Fifi':
(2,4), 'Fofona': (4,0)}
>>>			
>>> achei_uns_gatos(coord_gatos, (4,0))
>>> 
>>> achei_uns_gatos(coord_gatos, (10,10))
>>> 
