import os
existencias_arroz = 0
existencias_queso = 0
existencias_frijol = 0
def fnt_limpiar():
    os.system('cls')
    print('Autor: Valentina Arias')
    print('Version: V1.0')
    print('Fecha: 2024-19-03')
    fnt_existencias()
def fnt_existencias():
    global existencias_arroz
    global existencias_queso
    global existencias_queso
    print('\n<<<EXISTENCIAS ACTUALES>>>')
    print(f'\nARROZ X BULTO 250KG............ {existencias_arroz}')
    print(f'\nQUESO X BLOQUE 10KG............{existencias_queso}')
    print(f'\nFRIJOL X BULTO 150KG...........{existencias_frijol}')
def fnt_entrada(op):
    global existencias_arroz
    global existencias_queso
    global existencias_frijol
    sw2 = True
    if op <1 or op >= 2:
        print('\nOPCIÓN NO VALIDA <ENTER>')
    elif op == 1:
        
        while sw2 == True:
            fnt_limpiar()
            opciones = int(input('\n<<<OPCIONES DE PRODUCTOS>>>\n1. ARROZ\n2. QUESO\n3. FRIJOL\n4. SALIR\n->'))
            if opciones == 4:
                sw2 = False
            if opciones >= 1 and opciones <= 3: 
                cantidad = int(input('\nCantidad---> '))
                if opciones == 1:
                    existencias_arroz += cantidad
                if opciones == 2:
                    existencias_queso += cantidad
                if opciones == 3:
                    existencias_frijol += cantidad
            
sw = True
while sw == True:
    fnt_limpiar()
    opciones = int(input('\n<<< MENÚ DE OPCIONES >>>\n1. REGISTRO DE PRODUCTOS\n2. SALIDA DE PRODUCTOS\n4. SALIR\n->'))
    fnt_entrada(opciones)