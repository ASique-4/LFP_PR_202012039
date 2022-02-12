from itertools import count


texto = [['nombre', ' reporte01'], [' grafica', ' barras'], [' titulo', ' reporte de ventas agosto'], [' titulox', ' producto'], [' tituloy', ' total'], ['titulox', ' titulox2'], [' tituloy', ' total2']]
repetido = True
total = 7
count = len(texto)
count2 = 0
totalj = len(texto)
while count2 <= len(texto):
    for idx in range(0,len(texto)):
            for jdx in range(0,len(texto)):
                if jdx >= count or idx >= count:
                    break
                print(idx,jdx)
                if str(texto[idx][0]).strip() == str(texto[jdx][0]).strip() and texto[jdx][0] != None and texto[idx][0] != None:
                    if jdx != idx:
                        if jdx < idx:
                            print(str(texto[jdx][1]))
                            texto.pop(jdx)
                            
                        else:
                            print(str(texto[idx][1]))
                            texto.pop(idx)
                            
                        count -=1
                        break
    count2 +=1
