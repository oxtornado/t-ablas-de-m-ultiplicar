# Centro de Biotecnologia Agropecuaria
# Fecha: 13/06/24
# Aprendiz: Daniel Alexander Duarte Ussa
# Ficha: 2877795
# Version: 3.12.2


# Importamos Randint de la libreria random, para generar asi
# el numero hasta el que se van a generar las tablas
from random import randint
from modules.functions import *


def main():

    # Variable encargada de decidir hasta que tablas se generaran las tablas
    tabla_hasta_numero_aleatorio = randint(1, 20+1)

    #Este contador sera la tabla en la que comenzaremos hasta el numero aleatorio
    # En un ejemplo:


    # esta es la variable 'contador_de_tablas'
    # |
    # v
    # 1 x ***NUMEROS DEL 1 AL 10*** = ***RESULTADO***

    contador_de_tablas = 1


    # Informa cual es el numero aleatorio, en caso de ser 
    # lo unico que quiera saber el usuario
    print(f'El numero aleatorio es {tabla_hasta_numero_aleatorio}')

    # Es necesario un bucle, para llegar hasta el numero aleatorio
    while contador_de_tablas <= tabla_hasta_numero_aleatorio:

        # Muestra la tabla en la que se encuentra
        print(f'Tabla del {contador_de_tablas}')


    # Este indice sera los numeros del uno al 10
    # En un ejemplo:


    # esta es la variable 'indice_de_tabla'
    #               |
    #               v
    # 1 x ***NUMEROS DEL 1 AL 10*** = ***RESULTADO***
        indice_de_tabla = 1

        # Se invoca la funcion que pregunta si desea 
        # continuar con la generacion de tablas
        continuar_generando_tablas()

        # Bucle que se ejecuta sumando la varibale 'indice_de_tabla' hasta 
        # llegar a 10 que es convencionalmente, hasta donde llegan las 
        # tablas de multiplicar
        while indice_de_tabla <= 10:

            # Se imprimen las tablas con las variables 'indice_de_tabla' y 'contador_de_tablas'  
            print(f'{contador_de_tablas} x {indice_de_tabla} = {contador_de_tablas * indice_de_tabla}')
            
            # Se va sumando de uno en uno el indice de la tabla
            indice_de_tabla += 1
        #Se va sumando el contador hasta llegar a la variable 'tabla_hasta_numero_aleatorio' 
        contador_de_tablas += 1

    # Se llama a la funcion encargada del control de flujo
    # de la desicion sobre continuar generando tablas

    resp = continuar_tablar()
    if resp == 'no':
        exit()
    main()
    
# Condicion considerada buena practica para 
# llevar a cabo una modularizacion 'responsable'
if __name__ == '__main__':
    main()