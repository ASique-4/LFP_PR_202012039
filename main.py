
import PySimpleGUI as sg
intrucciones_glob = ''
datos_glob = ''
def PlotDeBarras(datos,instr):
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
    plt.ylabel('Cantidad de usuarios')
    
    ## Legenda en el eje x
    plt.xlabel('Lenguajes de programación')
    
    ## Título de Gráfica
    plt.title('Usuarios de lenguajes de programación')
    
    ## Mostramos Gráfica
    plt.show()
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
            titulo = titulo+','
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

def AnalizarInstrucciones(instrucciones1):
    file = open(instrucciones1, 'r') 
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



    texto = eval(texto)

    for idx in range(total):

        if str(texto[idx][0]).strip() == 'nombre' or str(texto[idx][0]).strip() == 'grafica':
            for jdx in range(total):
                if jdx != idx:
                    if texto[jdx][0].strip() == 'nombre' or texto[jdx][0].strip() == 'grafica' :
                        cumple = True
                        break

    if cumple == False:
        print('No se puede analizar porque al archivo .lfp le faltan instrucciones')


    file.close() 
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

            PlotDeBarras(AnalizarDatos(datos_glob),AnalizarInstrucciones(intrucciones_glob))
        else:
            print('Agregue los archivos de Datos e Instrucciones antes de analizar')
        print('>< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><')
    elif opcion == 4:
        print('>< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><')
        print("Opcion 4")   
        print('>< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><') 
    elif opcion == 5:

        salir = True
    else:
        print ("Introduce un numero entre 1 y 5")
 
print ("Fin")

