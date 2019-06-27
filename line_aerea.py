#Funcion que muestra la matriz que representa la ubicacion de los asientos
def ver_asiento(z):
    for i in z:
        for j in i:
            print(j,end=" ")
        print()
        
#Funcion que marca con X en la matriz la coordenada ingresada       
def asignar_asiento(x,y):
    if y=="A":
        y=0
    if y=="B":
        y=1
    if y=="C":
        y=2
    if y=="D":
        y=3
    if y=="E":
        y=4
    if y=="F":
        y=5
    if x=="01":
        x=0
    if x=="02":
        x=1
    if x=="03":
        x=2
    if x=="04":
        x=3
    if x=="05":
        x=4
    if x=="06":
        x=5
    if x=="07":
        x=6
    if x=="08":
        x=7
    if x=="09":
        x=8
    if x=="10":
        x=9
    if x=="17":
        x=10
    if x=="18":
        x=11
    if x=="19":
        x=12
    if x=="20":
        x=13
    if x=="21":
        x=14
    if x=="22":
        x=15
    if x=="23":
        x=16
    if x=="24":
        x=17
    if x=="25":
        x=18
    if x=="26":
        x=19
    if x=="27":
        x=20
    if x=="28":
        x=21
    if x=="29":
        x=22
    if x=="30":
        x=23
    if x=="31":
        x=24
    if x=="32":
        x=25
    if x=="33":
        x=26
  
    matriz[x][y]=matriz[x][y].replace(" ","x")

matriz=[["A01[ ]","B01[ ]","C01[ ]","D01[ ]","E01[ ]","F01[ ]"],
["A02[ ]","B02[ ]","C02[ ]","D02[ ]","E02[ ]","F02[ ]"],
["A03[ ]","B03[ ]","C03[ ]","D03[ ]","E03[ ]","F03[ ]"],
["A04[ ]","B04[ ]","C04[ ]","D04[ ]","E04[ ]","F04[ ]"],
["A05[ ]","B05[ ]","C05[ ]","D05[ ]","E05[ ]","F05[ ]"],
["A06[ ]","B06[ ]","C06[ ]","D06[ ]","E06[ ]","F06[ ]"],
["A07[ ]","B07[ ]","C07[ ]","D07[ ]","E07[ ]","F07[ ]"],
["A08[ ]","B08[ ]","C08[ ]","D08[ ]","E08[ ]","F08[ ]"],
["A09[ ]","B09[ ]","C09[ ]","D09[ ]","E09[ ]","F09[ ]"],
["A10[ ]","B10[ ]","C10[ ]","D10[ ]","E10[ ]","F10[ ]"],
["A17[ ]","B17[ ]","C17[ ]","D17[ ]","E17[ ]","F17[ ]"],
["A18[ ]","B18[ ]","C18[ ]","D18[ ]","E18[ ]","F18[ ]"],
["A19[ ]","B19[ ]","C19[ ]","D19[ ]","E19[ ]","F19[ ]"],
["A20[ ]","B20[ ]","C20[ ]","D20[ ]","E20[ ]","F20[ ]"],
["A21[ ]","B21[ ]","C21[ ]","D21[ ]","E21[ ]","F21[ ]"],
["A22[ ]","B22[ ]","C22[ ]","D22[ ]","E22[ ]","F22[ ]"],
["A23[ ]","B23[ ]","C23[ ]","D23[ ]","E23[ ]","F23[ ]"],
["A24[ ]","B24[ ]","C24[ ]","D24[ ]","E24[ ]","F24[ ]"],
["A25[ ]","B25[ ]","C25[ ]","D25[ ]","E25[ ]","F25[ ]"],
["A26[ ]","B26[ ]","C26[ ]","D26[ ]","E26[ ]","F26[ ]"],
["A27[ ]","B27[ ]","C27[ ]","D27[ ]","E27[ ]","F27[ ]"],
["A28[ ]","B28[ ]","C28[ ]","D28[ ]","E28[ ]","F28[ ]"],
["A29[ ]","B29[ ]","C29[ ]","D29[ ]","E29[ ]","F29[ ]"],
["A30[ ]","B30[ ]","C30[ ]","D30[ ]","E30[ ]","F30[ ]"],
["A31[ ]","B31[ ]","C31[ ]","D31[ ]","E31[ ]","F31[ ]"],
["A32[ ]","B32[ ]","C32[ ]","D32[ ]","E32[ ]","F32[ ]"],
["A33[ ]","B33[ ]","C33[ ]","D33[ ]","E33[ ]","F33[ ]"]]
#opcion venta de pasajes 
opcion=0
asientos=0
while opcion!=2:
    print("\nVENTA DE PASAJES")
    opcion=input("1) Asignar asiento\n2) Salir\n\nIngrese una opción: ")   
    while opcion.isdigit()==False:
        opcion=input("Ingrese una opción del menú: ")
    opcion=int(opcion)
    while opcion <1 or opcion >2:
        opcion=input("Ingrese una opción del menú: ")
        while opcion.isdigit()==False:
            opcion=input("Ingrese una opción del menú: ")
        opcion=int(opcion)
   
    if opcion==1:
        print("\n     ***ASIENTOS DISPONIBLES***\n")
        ver_asiento(matriz)
        print("\nASIGNAR ASIENTO")        
        cant_asientos=input("Ingrese numero de asientos que desea reservar (máximo 20): ")   
        while cant_asientos.isdigit()==False:
            cant_asientos =input("Ingrese solo numeros: ")
        cant_asientos =int(cant_asientos)
        while cant_asientos >20 or cant_asientos <1:
            cant_asientos =input("Minimo 1 asiento y maximo 20 asientos: ")
            while cant_asientos.isdigit()==False:
                cant_asientos =input("Ingrese solo numeros: ")
        cant_asientos =int(cant_asientos)
#acumulador que pide coordenadas hasta completar el total de pasajes solicitados
        while cant_asientos >asientos:
            asientos = asientos +1
            print("Ingrese las coordenadas del asiento n°", asientos,": ")
            letra=input("letra: ")
            letra=letra.upper()
            while letra.isalpha()==False:
                letra=input("Ingrese solo letras: ")
                letra=letra.upper()
            numero=input("numero: ")
            if len(numero)==1:
                numero = numero.zfill(2)
            while numero.isdigit()==False:
                numero=input("Ingrese solo numeros: ")
                if len(numero)==1:
                    numero = numero.zfill(2)
            numero=int(numero)
            print("antes del while",numero)
            primero=0
            segundo=0
            while primero==0 or segundo==0:
                print("dento del while 0 0")
                while numero>10 and numero<17:
                    print("while 10-17: ",numero)
                    print("asientos no disponibles")
                    numero=input("numero: ")
                    if len(numero)==1:
                        numero = numero.zfill(2)
                        print("while 10-17 2: ",numero)
                    while numero.isdigit()==False:
                        numero=input("Ingrese solo numeros: ")
                        if len(numero)==1:
                            numero = numero.zfill(2)
                    numero=int(numero)
                
                primero=1
                while numero<0 or numero>33:
                    print("while 0-33: ",numero)
                    print("asientos no disponibles")
                    numero=input("numero: ")
                    
                    if len(numero)==1:
                        numero = numero.zfill(2)
                        print("while 0-33 2: ",numero)
                    while numero.isdigit()==False:
                        numero=input("Ingrese solo numeros: ")
                        if len(numero)==1:
                            numero = numero.zfill(2)
                    numero=int(numero)
                   
                segundo=1
            numero=str(numero)
            if len(numero)==1:
                numero = numero.zfill(2)
           #muestra la matriz actualizada        
            
    asignar_asiento(numero,letra)
    ver_asiento(matriz)
    cant_asientos=0
    asientos=0