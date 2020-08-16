import pandas as pd
archivo = input()
datos = pd.read_csv(archivo, header=0, sep=';')
