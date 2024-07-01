# Centro de Biotecnologia Agropecuaria
# Fecha: 13/06/24
# Aprendiz: Daniel Alexander Duarte Ussa
# Ficha: 2877795
# Version: 3.12.2
# Nombramos la funcion que controlara la ejecucion del programa
def continuar_generando_tablas():
    # Un bucle que se ejecute hasta que la desicion esperada no se cumpla
    while True:    

        # Control para que el usuario digite su desicion de continuar
        print('Presione enter para continuar o digite no para terminar.')
        input_continuar_generando_tablas = input('Continuar con la siguiente tabla: ').lower()

        # Si la desicion es diferente de no, seguira generando tablas
        if input_continuar_generando_tablas != 'no':
            break
        elif input_continuar_generando_tablas == 'no':
            print('Hasta luego.')
            exit()



def continuar_tablar():
    while True:
        print('Presione enter para continuar o no para terminar')
        seguir_generando_tablas = input('Continuar generando tablas: ')
        if seguir_generando_tablas != 'no':
            break
        elif seguir_generando_tablas == 'no':
            print('Hasta luego')      
    return seguir_generando_tablas
