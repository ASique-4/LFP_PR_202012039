from operator import itemgetter
def AnalizarDatos(datos):
    file = open(datos, 'r') 
    inicio = False
    datos=[]
    titulobool = True
    texto = '['
    titulo = ''
    while 1: 
        char = file.read(1) 
        if char == ';':
            texto = texto+','
        if titulobool == True and char != ':' and char != '=':
            titulo = titulo+char.strip()
        if char == ':':
            titulo = titulo+'-'
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
            break 
        
    datos = eval(texto)

    datos.append(titulo)

    file.close() 
    return datos

def merge(list1, list2): 
      
    merged_list = [[list1[i], list2[i]] for i in range(0, len(list1))] 
    return merged_list 

def sort(datos):

    ganancias =[]
    for idx in range(len(datos)-1):
        ganancias.append(datos[idx][0])


    ganancias2 = []
    for idx in range(len(datos)-1):
        num = int(datos[idx][1])*int(datos[idx][2])
        ganancias2.append(num)

    lista = []
    lista = merge(ganancias,ganancias2)
    print(lista)
    print('-------------------------')
    print(sorted(lista, key=itemgetter(1),reverse=True))
    lista = sorted(lista, key=itemgetter(1),reverse=True)
    f = open('pruebaloop.html','w')
    mensaje = ''
    for i in range(len(lista)):
        mensaje +="""
        <td width="50%">"""+str(lista[i][0]).upper()+"""</td>
        <td width="50%">"""+str(lista[i][1])+"""</td>
        """
    f.write(mensaje)
    f.close()

sort(AnalizarDatos('Data.data'))

