import numpy as np
import csv

class Plan:

    __matriz = np
    __materias = str
    __size = int

    def __init__(self, size):

        self.__size = size
        self.__matriz_relaciones = np.zeros((size,size + 2), dtype = object)

    def csv_load(self):

        with open("correlativas.csv", "r", encoding="utf-8") as f:

            archi = csv.reader(f)

        
        
            for index, line in enumerate(archi):

                # print(f"el largo de la cadena es {type(line[4])}")
                # print(f"el indice es {index}")
                
                try:

                    # print(f"el numero int es {int(line[4])}")
                    digito_unico = int(line[4])
                    if(int(line[1]) == 1):

                        semestre = (int(line[0]) * 2) - 1

                    else:

                        semestre = (int(line[0]) * 2)


                    self.__insertar(semestre, index, line[4])
                
                except:

                    if line[4] != "":


                        correlativas = line[4].split(";")

                        if(int(line[1]) == 1):

                            semestre = (int(line[0]) * 2) - 1

                        else:

                            semestre = (int(line[0]) * 2)
                        
                        for correlativa in correlativas:


                            self.__insertar(semestre, index, int(correlativa), line[3])
                    
                    else:

                        if(int(line[1]) == 1):

                            semestre = (int(line[0]) * 2) - 1

                        else:

                            semestre = (int(line[0]) * 2)

                        self.__insertar(semestre, index, None, line[3])



                    
                        

    def __insertar(self, semestre, materia_origen, materia_destino, nombre):

        if(materia_destino == None):

            self.__matriz_relaciones[materia_origen][self.__size] = semestre
            self.__matriz_relaciones[materia_origen][self.__size + 1] = nombre

        else:
        
            self.__matriz_relaciones[materia_origen][materia_destino - 1] = 1
            self.__matriz_relaciones[materia_origen][self.__size] = semestre
            self.__matriz_relaciones[materia_origen][self.__size + 1] = nombre

    def save(self):

        csv_file_path = 'output.csv'


        np.savetxt(csv_file_path, self.__matriz_relaciones, delimiter=',', fmt='%s')

    def print_matriz(self):

        return print(self.__matriz_relaciones)
    
    def print_plan(self):

        for i in range(self.__size):
            
            if(self.__matriz_relaciones[i][self.__size] != 0):
                print((f"semestre: {self.__matriz_relaciones[i][self.__size]} materia {self.__matriz_relaciones[i][self.__size + 1]}"))

    def recursar(self, cod):
        
       

        set_1 = set()

       

        # if isinstance(cod, list):

        for elem in cod:
                
            elem = elem - 1
                
            set_1.add(elem)

            self.__recursada_recursiva(elem, set_1)

        set_2 = set()

        for element in set_1:

            nuevo = element + 1

            set_2.add(nuevo)

        print(set_2)

        

        for elem in set_1:

            self.__matriz_relaciones[elem][self.__size] += 2

    def __recursada_recursiva(self, cod, set_1):

       

       
        for i in range(self.__size):

            print(i)

            if self.__matriz_relaciones[i][cod] == 1:
                
                set_1.add(i)

                self.__recursada_recursiva(i, set_1)


        

plancito = Plan(36)
plancito.csv_load()

plancito.recursar([23])
plancito.print_plan()
plancito.save()
plancito.print_matriz()