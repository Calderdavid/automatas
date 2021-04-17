''' 
Cadenas que terminan en 101 
es un archivo contaminado, corrupto(C), 
si la cadena contiene entre 3 o 4 unos(111; 1111) 
o ceros(000; 0000) consecutivos se considara corrupto(C).

(L)impio
(C)orrupto

'''
def salida(cadena, flag, flag2):
    if flag == 1 and flag2 == 1:
        print(cadena.rstrip() + " "+ "(C)")
    else:
        print(cadena.rstrip() + " "+ "(L)")
    


def Automata(file):
    document = open(file, 'r')

    for line in document: #Por cada linea en el documento
        flag = 0
        flag2 = 0

        i = 0
        while i <= len(line): #Recorremos la linea
            end = len(line) - 4 #para no recorrer un indice que no existe en la memoria
            if i <= end:
                if line[i] == '0' and line[i+1] == '0' and line[i+2] == '0': 
                    flag2 = 1
                    break
                elif line[i] == '1' and line[i+1] == '1' and line[i+2] == '1' and line[i+3] == '1':
                    flag2 = 1
                    break
            i = i + 1
        
        if(line[-4] == '1' and line[-3] == '0' and line[-2] == '1'): #Si termina en 101
            flag = 1

        salida(line, flag, flag2)        

    document.close()



def main():

    file = 'testP1.txt' #returns an object with the read method
    Automata(file)

main()



