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
    one_cero_counter = 0
    counter = 0

    # for line in file:
    #     print(line[-4:-1])
    #     print(line[-4], line[-3], line[-2])
    
    for line in file:
        flag = 0
        flag2 = 0
        # print(type(line))
        # for letter in line:
        i = 0
        while i <= len(line):
            end = len(line) - 4
            if i <= end:
                if line[i] == '0' and line[i+1] == '0' and line[i+2] == '0':
                    # print(line[i], line[i+1], line[i+2])
                    flag2 = 1
                    one_cero_counter += 1
                    break
                elif line[i] == '1' and line[i+1] == '1' and line[i+2] == '1' and line[i+3] == '1':
                    flag2 = 1
                    one_cero_counter += 1
                    break
            i = i + 1
        
        if(line[-4] == '1' and line[-3] == '0' and line[-2] == '1'): #funcional
            flag = 1
            counter = counter + 1

        
        if flag == 1 and flag2 == 1:
            print('corrupto')
        else:
            print('limpio')
        
    
    file.close()
main()



