
#Exercise 1
text = "X-DSPAM-Confidence:		0.8475"
number = text.find(':')
number_1 = text[number + 1 : ]
# Esto no es necesario, al convertir a flotante la cadena elimina los espacios.
# ws = number_1.strip()
gone= float(number_1)
print (gone)