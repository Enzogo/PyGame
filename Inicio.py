
a =int(input("Presione 1 para registrarse: "))
if (a==1):
    print("Has Seleccionado el registro")
    Nombre= input("Ingrese Nombre y apellido:  " )
    telefono = int(input("Ingrese su Numero de telefono:  "))
    fecha = input("Ingrese Su fecha de nacimiento:  ")
    Rut = input("Ingrese su Rut: ")
    a = 0
    a = int(input("Te Has Registrado con exito!! Deseas Salir o Iniciar Carrera (1.Salir 2.Carrera)"))
    while (a > 2 or a < 1):
        a= int(input("Has Usado un Numero Erroneo Ingrese Otra vez: "))
if (a==1):
    print("Fin de La aplicacion")
    
if (a==2):
    print(" \n Hola",Nombre)
    
    print("Has Iniciado la Carrera: ")
    Pago  = 0
    Total = 0
    print("Cada 10 km/h aumentando sube el costo de 130 Pesos")
    Latitud =input("Ingrese Latitud de la carrera del vehiculo: (Norte,Sur,Este,Oeste): ")
    Longitud =float(input("Distancia de Recorrido iniciado: "))
    
c = int(input("Quieres Encender el Vehiculo (1.Si 2.No): "))
while (c > 3 or c < 1):
    c =int(input("Opcion no Valida Ingresa Nuevamente la Opcion:  ")) 
Velocidad = 0
while (c==1):
        Hora = float(input("Has Subido a Las (Horas):"))
        min = float(input("Con Min: "))
        pm = input("PM o AM?: ")
        print("Vas Viajando al: ",Latitud,"\n con una Distacion de recorrido de: ",Longitud)
        print("Vas a una velocidad de X KM/h: ")
        acelerar= int(input("Deseas Accelerar (1.Si 2.No): "))
    
        while (acelerar==1):
              acelerar=1
              Velocidad = Velocidad + 10
              Longitud = Longitud + 10
              min = min + 5
              if (min== 60):
                  hora = hora + 1
                  min = 0
              Pago = Pago + 130
              print("Te encuentra A la Velocidad de: ",Velocidad)
              acelerar= int(input("Desear seguir Acelerando (1.Si 2.No) "))
        
        print("Vas A una Velocidad de: ",Velocidad)
    
        girar = int(input("Deseas Girar? (1.Si 2.No)"))
    
        while (girar==1):
                 direccion=(input("(Viras 1.Oeste o 2.Este): "))
                 print("Vas al: ",Latitud,"Has Girado hacia la: ",direccion)
                 print("Has Girado en el cual fuiste a 5 km/h ")
                 Longitud = Longitud + 5
                 Pago = Pago + 75
                 girar = 2
        if (girar==2):
             c=int(input("Te Preguntan ¿Llegaste a tu Destino? (1.No 2.si) "))
    
if (c==2):
    print("Has Viajado en total: ",Longitud,"KM")
    print("Viajando al: ",Latitud,"con viracion a: ",direccion)
    print("Terminando el Viaje a las: ",Hora,"Con ",min)
    Total = (Longitud + Velocidad) * Pago / 10
    print("Has frenado y se te ha generado un cobro:",Total,"Pesos")
         

    
    
    
        