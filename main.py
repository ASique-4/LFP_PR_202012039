from PIL import Image
from operator import itemgetter
from re import T
import PySimpleGUI as sg
from matplotlib.pyplot import plot
nombre_del_grafico = []
HayTitulo = False
Titulo = []
Titulo2 = ['REPORTE DE VENTAS ']
HayTitulox = False
Tituloy = []
HayTituloy = False
Titulox=[]
intrucciones_glob = ''
datos_glob = ''
tipo_de_grafico = []
def merge(list1, list2): 
      
    merged_list = [[list1[i], list2[i]] for i in range(0, len(list1))] 
    return merged_list 



def CrearReportes(datos):
    
    ganancias =[]
    for idx in range(len(datos)-1):
        ganancias.append(datos[idx][0])

    ganancias2 = []
    for jdx in range(len(datos)-1):
        num = int(datos[jdx][1])*int(datos[jdx][2])
        ganancias2.append(num)

    lista = []
    lista = merge(ganancias,ganancias2)
    lista = sorted(lista, key=itemgetter(1),reverse=True)

    f = open('holamundo.html','w')

    mensaje = """<html>
    <head><title> REPORTE DE VENTAS </title>
        <style>
        </style>
    </head>
    
    <body bgcolor=" #72c1af ">
        <h1 style="text-align: center; color: bisque;">Angel Francisco Sique Santos -- 202012039</h1>
        <table align="center" border="1" cellpadding="0" cellspacing="0" width="50%">
            <tr>
            <td style="font-family:'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;" width="50%" bgcolor="#33c1ff " align="center">Producto</td>
            <td style="font-family:'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;" width="50%" bgcolor=" #42ff33 " align="center">Ganancias</td>
            </tr>
            <tr>
            """ 
    for i in range(len(lista)):
        mensaje +="""
        <tr>
        <td  bgcolor=" #c6f5eb " width="50%">"""+str(lista[i][0]).upper()+"""</td>
        <td width="50%" bgcolor=" #c6f5eb " align="center">"""+str(lista[i][1])+"""</td>
        </tr>
        """
    
    mensaje += """
        </tr>
        </table>"""
    mensaje +="""
    <table align="center" border="1" cellpadding="0" cellspacing="0" width="50%">
            <tr>
            <td style="font-family:'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;" width="50%" bgcolor="#33c1ff " align="center">Producto Más Vendido</td>
            <td style="font-family:'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;" width="50%" bgcolor=" #33c1ff " align="center">Producto Menos Vendido</td>
            </tr>
            <tr>
        <tr>
        <td  bgcolor=" #c6f5eb " width="50%" align="center">"""+str(lista[0][0]).upper()+"""</td>
        <td width="50%" bgcolor=" #c6f5eb " align="center">"""+str(lista[len(lista)-1][0]).upper()+"""</td>
        </tr>
        """
    mensaje +="""
    </body>
</html>"""

    f.write(mensaje)
    f.close()
def PlotDePastel(datos):
    import matplotlib.pyplot as plt
    ## Declaramos valores para el eje x
    eje_x = []
    for idx in range(len(datos)-1):
        eje_x.append(datos[idx][0])

    ## Declaramos valores para el eje y
    eje_y = []
    for idx in range(len(datos)-1):
        num = int(datos[idx][1])*int(datos[idx][2])
        eje_y.append(num)
    
    
    ## Creamos Gráfica
    plt.pie(eje_y,labels=eje_x)
    
    ## Título de Gráfica
    if Titulo != None and Titulo != '' and Titulo != []:
        plt.title(Titulo[0])
    else:
        titulo_grf = str(Titulo2[0])+str(Titulo2[1].upper())
        plt.title(titulo_grf)
    plt.savefig(str(nombre_del_grafico[0])+'.jpg')
    imagen = Image.open(str(nombre_del_grafico[0])+'.jpg')
    imagen.show()
def PlotDeLineas(datos):
    import matplotlib.pyplot as plt
    ## Declaramos valores para el eje x
    eje_x = []
    for idx in range(len(datos)-1):
        eje_x.append(datos[idx][0])

    ## Declaramos valores para el eje y
    eje_y = []
    for idx in range(len(datos)-1):
        num = int(datos[idx][1])*int(datos[idx][2])
        eje_y.append(num)
    
    
    ## Creamos Gráfica
    fig, ax = plt.subplots()
    ax.plot(eje_x, eje_y)
    
    ## Legenda en el eje y
    if Tituloy != None and Tituloy != '' and Tituloy != []:
        plt.ylabel(Tituloy[0].upper())
    else:
        plt.ylabel('')
    
    ## Legenda en el eje x
    if Titulox != None and Titulox != '' and Titulox != []:
        plt.xlabel(Titulox[0].upper())
    else:
        plt.xlabel('')
    
    
    ## Título de Gráfica
    if Titulo != None and Titulo != '' and Titulo != []:
        plt.title(Titulo[0])
    else:
        titulo_grf = str(Titulo2[0])+str(Titulo2[1].upper())
        plt.title(titulo_grf)
    plt.savefig(str(nombre_del_grafico[0])+'.jpg')
    imagen = Image.open(str(nombre_del_grafico[0])+'.jpg')
    imagen.show()
def PlotDeBarras(datos):
    import matplotlib.pyplot as plt
    ## Declaramos valores para el eje x
    eje_x = []
    for idx in range(len(datos)-1):
        eje_x.append(datos[idx][0])

    ## Declaramos valores para el eje y
    eje_y = []
    for idx in range(len(datos)-1):
        num = int(datos[idx][1])*int(datos[idx][2])
        eje_y.append(num)
    
    
    ## Creamos Gráfica
    plt.bar(eje_x, eje_y)
    
    ## Legenda en el eje y
    if Tituloy != None and Tituloy != '' and Tituloy != []:
        plt.ylabel(Tituloy[0].upper())
    else:
        plt.ylabel('')
    
    ## Legenda en el eje x
    if Titulox != None and Titulox != '' and Titulox != []:
        plt.xlabel(Titulox[0].upper())
    else:
        plt.xlabel('')
    
    
    ## Título de Gráfica
    print(Titulo)
    if Titulo != None and Titulo != '' and Titulo != []:
        plt.title(Titulo[0])
    else:
        titulo_grf = str(Titulo2[0])+str(Titulo2[1].upper())
        plt.title(titulo_grf)
    
    
    ## Mostramos Gráfica
    plt.savefig(str(nombre_del_grafico[0])+'.jpg')
    imagen = Image.open(str(nombre_del_grafico[0])+'.jpg')
    imagen.show()
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
    Titulo2.append(titulo)

    file.close() 
    return datos
def AnalizarInstrucciones(instrucciones1):
    file = open(instrucciones1, 'r') 
    inicio = False
    cumple = False
    total = 0
    texto = "["
    while 1: 
        char = file.read(1) 
        if char == '?':
            texto = texto[:-6]
            texto += "']]"
            inicio = False
            break
        if char == ',':
            texto = texto+"'],['"
            total = total+1
        if char == '¿':
            texto += "['"
            inicio = True
        if char == ':':
            texto = texto+"','"
    
    
        if inicio == True:

            if char != '\n' and char != '' and char != None and char != '¿' and char != '"' and char != ':' and char != ',' and char != '?':
                texto = texto+char.lower()
        if not char:  

            break 



    texto = eval(texto)
    for idx in range(total):

        if str(texto[idx][0]).strip() == 'nombre' or str(texto[idx][0]).strip() == 'grafica':
            for jdx in range(total):
                if jdx != idx:
                    if texto[jdx][0].strip() == 'nombre' or texto[jdx][0].strip() == 'grafica' :
                        cumple = True
                        break
    count = len(texto)
    count2 = 0
    while count2 <= len(texto):
        for idx in range(0,len(texto)):
                for jdx in range(0,len(texto)):
                    if jdx >= count or idx >= count:
                        break
                    if str(texto[idx][0]).strip() == str(texto[jdx][0]).strip() and texto[jdx][0] != None and texto[idx][0] != None:
                        if jdx != idx:
                            if jdx < idx:
                                texto.pop(jdx)
                            else:
                                texto.pop(idx)    
                            count -=1
                            break
        count2 +=1
    
    total = len(texto)
    for idx in range(total):
        if str(texto[idx][0]).strip() == 'titulo':
            Titulo.append(texto[idx][1].upper())
            break
    for idx in range(total):
        if str(texto[idx][0]).strip() == 'tituloy' or str(texto[idx][0]).strip() == 'títuloy':
            Tituloy.append(texto[idx][1])
            break
    for idx in range(total):
        if str(texto[idx][0]).strip() == 'titulox' or str(texto[idx][0]).strip() == 'títulox':
            Titulox.append(texto[idx][1])
            break
    for idx in range(total):
        if str(texto[idx][0]).strip() == 'grafica' or str(texto[idx][0]).strip() == 'gráfica':
            tipo_de_grafico.append(texto[idx][1])
            break
    for idx in range(total):
        if str(texto[idx][0]).strip() == 'nombre':
            nombre_del_grafico.append(texto[idx][1])
            break
    file.close() 
    if cumple == False:
        print('No se puede analizar porque al archivo .lfp le faltan instrucciones')
    else:
        return texto
print('>< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><')
def pedirNumeroEntero():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce un numero entero: "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')
     
    return num
 
salir = False
opcion = 0
            
while not salir:
 
    print ("1. Cargar Datos")
    print ("2. Cargar Instrucciones")
    print ("3. Analizar")
    print ("4. Hacer Reportes")
    print ("5. Salir")
     
    print ("Elige una opcion")
 
    opcion = pedirNumeroEntero()

    if opcion == 1:
        print('>< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><')

        sg.theme('Dark Grey 13')   

        layout = [[sg.Text('Escoge el archivo .data')],
          [sg.Input(disabled = True , text_color='black' ), sg.FileBrowse(file_types=(("Data Files", "*.data"),))],
          [sg.OK(), sg.Cancel()]]

        window = sg.Window('Datos', layout)


        event, Datos = window.read()
        
        if Datos[0] == '' or Datos[0] == None or event == 'Cancel' or event == sg.WIN_CLOSED:
            print('No escogiste ningún archivo .data')
        else:
            print('Escogiste el archivo: ',Datos[0])
            datos_glob = Datos[0]
        window.close()

        print('>< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><')
    elif opcion == 2:
        print('>< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><')

        
        sg.theme('Dark Grey 13') 

        layout = [[sg.Text('Escoge el archivo .lfp')],
          [sg.Input(disabled = True , text_color='black'), sg.FileBrowse(file_types=(("lfp Files", "*.lfp"),))],
          [sg.OK(), sg.Cancel()]]


        window = sg.Window('Instrucciones', layout)


        event, Instrucciones = window.read()

        if Instrucciones[0] == '' or Instrucciones[0] == None or event == 'Cancel'  or event == sg.WIN_CLOSED:
            print('No escogiste ningún archivo')
        else:
            print('Escogiste el archivo: ',Instrucciones[0])
            intrucciones_glob = Instrucciones[0]
        window.close()
        print('>< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><')
    elif opcion == 3:
        print('>< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><')
        if intrucciones_glob != None and datos_glob != None and intrucciones_glob != '' and datos_glob != '':
            AnalizarInstrucciones(intrucciones_glob)
            
            if str(tipo_de_grafico[0]).strip() == 'barras':
                PlotDeBarras(AnalizarDatos(datos_glob))
            elif str(tipo_de_grafico[0]).strip() == 'lineas' or str(tipo_de_grafico[0]).strip() == 'líneas':
                PlotDeLineas(AnalizarDatos(datos_glob))
            elif str(tipo_de_grafico[0]).strip() == 'pie':
                PlotDePastel(AnalizarDatos(datos_glob))
            else:
                print('Algo salió mal')
        else:
            print('Agregue los archivos de Datos e Instrucciones antes de analizar')
        print('>< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><')
    elif opcion == 4:
        print('>< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><')
        if datos_glob != None and datos_glob != '': 
            print('Realizando reportes')
            CrearReportes(AnalizarDatos(datos_glob))
        else:
                print('Algo salió mal')
        print('>< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><') 
    elif opcion == 5:

        salir = True
    else:
        print ("Introduce un numero entre 1 y 5")
print('>< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><') 
print ("Fin")
print('>< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><')
