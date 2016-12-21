#Obtenha o valor da chave 'ano de nascimento', use o valor 'desconhecido'
#como valor pré-definido, para os seguintes dicionários:

#Pratique items(), keys() e values() com:

cat = {'idade': 9, 'cor': 'branca',
'sexo': 'fêmea'}

cat.get('ano de nascimento', 'desconhecido')

gatinho = {'idade': 1, 'cor': 'branca',
'sexo': 'fêmea', 'ano de nascimento':
'2015'}

gatinho.get('ano de nascimento')
gatinho.get('ano de nascimento', 'desconhecido')

cat
cat.items()
cat.keys()
cat.values()
