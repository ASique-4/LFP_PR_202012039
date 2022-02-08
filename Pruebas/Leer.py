from operator import length_hint
from re import T


file = open('Data.data', 'r') 
inicio = False
texto2=[]
titulobool = True
texto = '['
titulo = "'"
while 1: 
    char = file.read(1) 
    if char == ';':
        texto = texto+','
    if titulobool == True and char != ':' and char != '=':
        titulo = titulo+char.strip()
    if char == ':':
        titulo = titulo+"'-'"
    if char == '=':
        titulobool = False
    if char == '[':
        inicio = True
    if inicio == True:
        if char != '\n' and char != '' and char != None and char != ';':
            texto = texto+char.strip()
    if char == ';':
        inicio = False
    if not char:  
        texto = texto[:-1]
        texto = texto+']'
        titulo = titulo+"'"
        break 
    
texto2 = eval(texto)
print(texto2)
print('-------------------') 
titulo = '['+titulo+']'
texto2.append(eval(titulo))
print(texto2)
eje_y = []
for idx in range(len(texto2)-1):
    num = int(texto2[idx][1])*int(texto2[idx][2])
    eje_y.append(num)
    
print(eje_y)

file.close() 