import csv
my_file = "medellin_colombia-grande.txt"
i = 0
csv.register_dialect('skip_space', skipinitialspace=True)
with open(my_file, 'r') as f:
    reader=csv.reader(f , delimiter=' ', dialect='skip_space')
    
    for item in reader:
        print(item)
        #ignorar el for each y el print en caso de no querer imprimir la lista, todos los datos esta almacenados en la variable "reader"
      