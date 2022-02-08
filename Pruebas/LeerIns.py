

from matplotlib.pyplot import text


file = open('instrucciones.lfp', 'r') 
inicio = False
cumple = False
total = 0
texto = "[['"
while 1: 
    char = file.read(1) 
    if char == ',':
        texto = texto+"'],['"
        total = total+1
    if char == '¿':
        inicio = True
    if char == ':':
        texto = texto+"','"
    if char == '?':
        inicio = False
    
    if inicio == True:

        if char != '\n' and char != '' and char != None and char != '¿' and char != '"' and char != ':' and char != ',':
            texto = texto+char.lower()
    if not char:  
        texto = texto[:-2]
        texto = texto+']'
        break 

print(eval(texto))
print('-------------------') 
texto = eval(texto)
print(texto[0][0])
for idx in range(total):

    if str(texto[idx][0]).strip() == 'nombre' or str(texto[idx][0]).strip() == 'grafica':
        for jdx in range(total):
            if jdx != idx:
                if texto[jdx][0].strip() == 'nombre' or texto[jdx][0].strip() == 'grafica' :
                    cumple = True
                    print('Si')
                    break

if cumple == False:
    print('No se puede analizar porque al archivo .lfp le faltan instrucciones')


file.close() 