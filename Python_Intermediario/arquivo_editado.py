Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:16:31) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #Edite o módulo chamado arquivos.py. Nele, crie outra função chamada continua_escrevendo_novo_zen que leia zen.txt e que continue escrevendo sem apagar o que já estava em zen2.txt, somente as linhas que NÃO contiverem uma dada palavra. Neste módulo, execute a função e, em seguida, leia e mostre (print) o conteúdo de zen2.txt.
>>> def escreve_novo_zen(palavra):
	with open('zen.txt', 'r') as f:
		for linha in f:
			if palavra in linha:
				with open('zen2.txt', 'w') as f2:
					f2.write(linha)

					
>>> def continua_escrevendo_novo_zen(palavra):
	with open('zen.txt', 'r') as f:
		for linha in f:
			if not palavra in linha:
				with open ('zen2.txt', 'a') as f2:
					f2.write(linha)

					
>>> 
