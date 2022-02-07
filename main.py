
from msilib.schema import File

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
        import PySimpleGUI as sg
        sg.theme('Dark Grey 13')   

        layout = [[sg.Text('Escribe la ruta o navega entre los archivos')],
          [sg.Input(), sg.FileBrowse()],
          [sg.OK(), sg.Cancel()]]

        window = sg.Window('Datos', layout)


        event, Datos = window.read()
        
        if Datos[0] == '' or Datos[0] == None:
            print('No escogiste ningún archivo')
        else:
            print('Escogiste el archivo: ',Datos[0])
        window.close()

        print('>< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><')
    elif opcion == 2:
        print('>< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><')

        import PySimpleGUI as sg
        sg.theme('Dark Grey 13') 

        layout = [[sg.Text('Escribe la ruta o navega entre los archivos')],
          [sg.Input(), sg.FileBrowse()],
          [sg.OK(), sg.Cancel()]]


        window = sg.Window('Datos', layout)


        event, Instrucciones = window.read()
        
        if Instrucciones[0] == '' or Instrucciones[0] == None:
            print('No escogiste ningún archivo')
        else:
            print('Escogiste el archivo: ',Instrucciones[0])
        window.close()
        print('>< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><')
    elif opcion == 3:
        print('>< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><')
        print("Opcion 3")
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

