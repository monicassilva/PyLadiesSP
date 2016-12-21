Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:16:31) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
#Crie um módulo chamado arquivos.py. Nele, crie uma função chamada escreve_novo_zen que leia zen.txt, escreva em zen2.txt
#somente as linhas que contiverem uma dada palavra. Neste módulo,execute a função e, em seguida, leia e mostre (print) o conteúdo de zen2.txt.


>>> def escreve_novo_zen(palavra):
	with open('zen,txt', 'r') as f:
		if palavra in linha:
			with open('zen2.txt', 'w') as f2:
				f2.write(linha)
				escreve_novo_zen('is')
				with open('zen2.txt', 'r') as f:
					print(f.read())

					
>>> 
