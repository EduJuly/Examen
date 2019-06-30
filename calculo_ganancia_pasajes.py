as_comun=60000
as_espiernas=80000
no_reclina=50000
cantidad_as_comun=0
cantidad_as_espiernas=0
cantidad_no_reclina=0
pasajes=0
total_as_comun=0
total_as_espiernas=0
total_no_reclina=0
lista_asientos=(1,2,3,4,5,6,7,8,9,10,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33)


cant_reserva=input("Ingrese la cantidad de pasajes que desea reservar, mínimo 1 pasaje y maximo 20 pasajes: ")   
while cant_reserva.isdigit()==False:
    cant_reserva=input("Ingrese solo numeros: ")
cant_reserva=int(cant_reserva)
while cant_reserva>20 or cant_reserva<1:
    cant_reserva=input("Minimo 1 pasaje y maximo 20 pasajes: ")
    while cant_reserva.isdigit()==False:
        cant_reserva=input("Ingrese solo numeros: ")
    cant_reserva=int(cant_reserva)
  
while cant_reserva>pasajes:
    pasajes=pasajes+1
    print("Ingrese las coordenadas del pasaje n°",pasajes,": ")
    letra=input("letra: ")
    letra=letra.upper()
    while letra.isalpha()==False:
        letra=input("Ingrese solo letras: ")
        letra=letra.upper()
    numero=input("número: ")
    while numero.isdigit()==False:
        numero=input("Ingrese solo número: ")
    numero=int(numero)
    while numero not in lista_asientos:
        numero=input("Ubicación no disponible, ingrese otro numero: ")
        while numero.isdigit()==False:
            numero=input("Ingrese solo numeros:")
        numero=int(numero)
    
    if numero>0 and numero<6:
        cantidad_as_espiernas=cantidad_as_espiernas+1
        total_as_espiernas=total_as_espiernas+as_espiernas
    if numero==18:
        cantidad_as_comun=cantidad_as_comun+1
        total_as_espiernas=total_as_espiernas+as_espiernas    
    if numero>5 and numero<10:
        cantidad_as_comun=cantidad_as_comun+1
        total_as_comun=total_as_comun+as_comun
    if numero==10 or numero==17:
        cantidad_no_reclina=cantidad_no_reclina+1
        total_no_reclina=total_no_reclina+no_reclina  
          
total_cantidad=(cantidad_as_comun+cantidad_as_espiernas+cantidad_no_reclina)
total_dinero=(total_as_espiernas+total_as_comun+total_no_reclina)

print("\nDetalle Reserva Pasajes")
print("---------------------------------------")
print("Asiento común",as_comun,    cantidad_as_comun,  total_as_comun)
print("Esp p piernas",as_espiernas,    cantidad_as_espiernas,   total_as_espiernas)
print("No reclina" ,    no_reclina,   cantidad_no_reclina,   total_no_reclina)
print("---------------------------------------")
print("TOTAL",                              total_cantidad,       total_dinero)