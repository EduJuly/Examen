from colorama import init, Fore, Style
#Funcion que muestra la matriz que representa la ubicacion de los asientos, con colores distintivos segun tipo de asiento.
def ver_asiento(z):
    for i in z:
        for j in i:
            print(j,end=" ")
        print()
    print(Fore.BLUE+Style.BRIGHT+"\n\nASIENTO COMUN")
    print(Fore.GREEN+"ESPACIO ADICIONAL PARA PIERNAS") 
    print(Fore.RED+"NO RECLINA\n\n")
      

matriz=[[Fore.GREEN+Style.BRIGHT+"A01[ ]","B01[ ]","C01[ ]",Fore.BLACK+"__",Fore.GREEN+"D01[ ]","E01[ ]","F01[ ]"],
["A02[ ]","B02[ ]","C02[ ]",Fore.BLACK+"__",Fore.GREEN+"D02[ ]","E02[ ]","F02[ ]"],
["A03[ ]","B03[ ]","C03[ ]",Fore.BLACK+"__",Fore.GREEN+"D03[ ]","E03[ ]","F03[ ]"],
["A04[ ]","B04[ ]","C04[ ]",Fore.BLACK+"__",Fore.GREEN+"D04[ ]","E04[ ]","F04[ ]"],
["A05[ ]","B05[ ]","C05[ ]",Fore.BLACK+"__",Fore.GREEN+"D05[ ]","E05[ ]","F05[ ]"],
[Fore.BLUE+"A06[ ]","B06[ ]","C06[ ]",Fore.BLACK+"__",Fore.BLUE+"D06[ ]","E06[ ]","F06[ ]"],
["A07[ ]","B07[ ]","C07[ ]",Fore.BLACK+"__",Fore.BLUE+"D07[ ]","E07[ ]","F07[ ]"],
["A08[ ]","B08[ ]","C08[ ]",Fore.BLACK+"__",Fore.BLUE+"D08[ ]","E08[ ]","F08[ ]"],
["A09[ ]","B09[ ]","C09[ ]",Fore.BLACK+"__",Fore.BLUE+"D09[ ]","E09[ ]","F09[ ]"],
[Fore.RED+"A10[ ]","B10[ ]","C10[ ]",Fore.BLACK+"__",Fore.RED+"D10[ ]","E10[ ]","F10[ ]"],
["A17[ ]","B17[ ]","C17[ ]",Fore.BLACK+"__",Fore.RED+"D17[ ]","E17[ ]","F17[ ]"],
[Fore.GREEN+"A18[ ]","B18[ ]","C18[ ]",Fore.BLACK+"__",Fore.GREEN+"D18[ ]","E18[ ]","F18[ ]"],
[Fore.BLUE+"A19[ ]","B19[ ]","C19[ ]",Fore.BLACK+"__",Fore.BLUE+"D19[ ]","E19[ ]","F19[ ]"],
["A20[ ]","B20[ ]","C20[ ]",Fore.BLACK+"__",Fore.BLUE+"D20[ ]","E20[ ]","F20[ ]"],
["A21[ ]","B21[ ]","C21[ ]",Fore.BLACK+"__",Fore.BLUE+"D21[ ]","E21[ ]","F21[ ]"],
["A22[ ]","B22[ ]","C22[ ]",Fore.BLACK+"__",Fore.BLUE+"D22[ ]","E22[ ]","F22[ ]"],
["A23[ ]","B23[ ]","C23[ ]",Fore.BLACK+"__",Fore.BLUE+"D23[ ]","E23[ ]","F23[ ]"],
["A24[ ]","B24[ ]","C24[ ]",Fore.BLACK+"__",Fore.BLUE+"D24[ ]","E24[ ]","F24[ ]"],
["A25[ ]","B25[ ]","C25[ ]",Fore.BLACK+"__",Fore.BLUE+"D25[ ]","E25[ ]","F25[ ]"],
["A26[ ]","B26[ ]","C26[ ]",Fore.BLACK+"__",Fore.BLUE+"D26[ ]","E26[ ]","F26[ ]"],
["A27[ ]","B27[ ]","C27[ ]",Fore.BLACK+"__",Fore.BLUE+"D27[ ]","E27[ ]","F27[ ]"],
["A28[ ]","B28[ ]","C28[ ]",Fore.BLACK+"__",Fore.BLUE+"D28[ ]","E28[ ]","F28[ ]"],
["A29[ ]","B29[ ]","C29[ ]",Fore.BLACK+"__",Fore.BLUE+"D29[ ]","E29[ ]","F29[ ]"],
["A30[ ]","B30[ ]","C30[ ]",Fore.BLACK+"__",Fore.BLUE+"D30[ ]","E30[ ]","F30[ ]"],
["A31[ ]","B31[ ]","C31[ ]",Fore.BLACK+"__",Fore.BLUE+"D31[ ]","E31[ ]","F31[ ]"],
["A32[ ]","B32[ ]","C32[ ]",Fore.BLACK+"__",Fore.BLUE+"D32[ ]","E32[ ]","F32[ ]"],
["A33[ ]","B33[ ]","C33[ ]",Fore.BLACK+"__",Fore.BLUE+"D33[ ]","E33[ ]","F33[ ]"]]

ver_asiento(matriz)