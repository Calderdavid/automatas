''' 
Cadenas que terminan en 101 
es un archivo contaminado, corrupto(C), 
si la cadena contiene entre 3 o 4 unos(111; 1111) 
o ceros(000; 0000) consecutivos se considara corrupto(C).

(L)impio
(C)orrupto

'''

def main():

    file = open('testP1.txt', 'r') #returns an object with the read method
    list = []
    


    for line in file:
        # print(type(line))
        list.append(line)  #stores each line inside in the list

    # print(len(list))

    flag = 0
    cero_counters = 0
    one_counters = 0
    i = 0
    while one_counters < 3 && cero_counters < 3 :
        temp = list[i]

        if(temp[-3] == 1 && temp[-2] == 0 && temp[-1] == 1):
            flag = 1


        for letter in temp:
            if(letter == 0):
                cero_counter += 1
            else:
                one_counters += 1
        
        i = i + 1
    
    

    
    


        


main()



