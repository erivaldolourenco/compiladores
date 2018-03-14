#teste de hashmap
# import re
# lexema = ' int entrance()\n'
# print(list(lexema))
# for letra in list(lexema):
# 	print("--"+letra+"--")
# 	if re.findall('[^A-Za-z0-9]',letra):
# 		print("CARACTER ESPECIAL")
# 	if letra == '(':
# 		print("ABREPARENTES")
# 	if letra == '\n':
# 		print("FIM DE LINHA")
position = [0,0]
position[1] = 10
teste = "erivaldo lourenco mariano"
for i  in range(position[1],int(teste.__len__())):
	print(teste[i])