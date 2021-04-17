''' 
Cadenas que terminan en 101 
es un archivo contaminado, corrupto(C), si la cadena contiene entre 3 o 4 unos(111; 1111) o ceros(000; 0000) consecutivos se considara corrupto(C).

(L)impio
(C)orrupto

'''
#
#variables

def buscar(mensaje,contaminacion,dummy):

  if(contaminacion==1):
    print("".join(mensaje) + " "+ "(C)")
  else:
    print("".join(mensaje) + " "+ "(L)")
  dummy = 0
  return dummy

def main():#funcion principal

  file = open("testP1.txt","r")
  Lines = file.read().splitlines()
  #inicio de codigo:

  for line in Lines:
    contaminacion = 0
    a=0
    b=1
    c=2
    d=3
    dummy = 1
    mensaje = list(line)
    #print(mensaje)
    largo_lista = len(mensaje)-1
    #print(largo_lista)
    if(largo_lista != 0):
      #siguiente linea
      while ( dummy != 0):
        
        try:
          if (d == largo_lista):
            if (mensaje[b] == "1" and mensaje[c] == "0" and mensaje[d] == "1"):
              #print("CASO 7")
              contaminacion = 1
            elif (mensaje[b] == "1" and mensaje[c] == "1" and mensaje[d] == "1"):
              ##print("CASO 3")
              contaminacion = 1
            elif (mensaje[b] == "0" and mensaje[c] == "0" and mensaje[d] == "0"):
              ##print("CASO 4")
              contaminacion = 1
            dummy = buscar(mensaje,contaminacion,dummy)
          elif (mensaje[a] == "1" and mensaje[b] == "1" and mensaje[c] == "1"):
            contaminacion = 1
            ##print("CASO 1")
          elif (mensaje[a] == "0" and mensaje[b] == "0" and mensaje[c] == "0"):
           # #print("CASO 2")
            contaminacion = 1
          elif (mensaje[a] == "1" and mensaje[b] == "1" and mensaje[c] == "1" and mensaje[d] == "1"):
            #print("CASO 5")
            contaminacion = 1
        
          elif (mensaje[a] == "0" and mensaje[b] == "0" and mensaje[c] == "0" and mensaje[d] == "0"):
            #print("CASO 6")
            contaminacion = 1
        except IndexError:
          print("Ha ocurrido un error desconocido, saltando linea...")
        a = a +1
        b = b +1
        c = c +1
        d = d +1
  #print("fin")
  file.close()

main()