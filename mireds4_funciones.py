from datetime import datetime
#Hola.
#En esta ocasiÃ³n vamos a continuar con el cÃ³digo de nuestra red social,
#al cual le habÃ­amos agregado un menÃº.
#
#El programa de la semana anterior permitÃ­a:
#1. Obtener datos del usuario
#2. Consultar y mostrar varios mensajes de estado del usuario
#3. Escoger entre distintas acciones que el usuario puede realizar
#

#Si lograste agregar una opción nueva al sistema, por ejemplo, para escribir los datos
#del perfil del usuario, habrÃ¡s notado que tienes que escribir de nuevo el cÃ³digo necesario
#con un print por cada dato. El cÃ³digo se verÃ­a como estÃ¡ más abajo.

def mostrar_bienvenida():
    print("Bienvenido a ... ")
    print("""
                  _                  __
       ____ ___  (_)  ________  ____/ /
      / __ `__ \/ /  / ___/ _ \/ __  /
     / / / / / / /  / /  /  __/ /_/ /
    /_/ /_/ /_/_/  /_/   \___/\__,_/

    """)

# Solicitud de nombre
def obtener_nombre():
    nombre = input("Para empezar, dime como te llamas.").capitalize()
    print()
    print(f"Hola {nombre}, bienvenido a Mi Red")
    print()
    return nombre

# CÃ¡lculo de edad
def obtener_edad():
    agno = int(input("Para preparar tu perfil, dime en qué año naciste. "))
    edad = datetime.now().year-agno-1
    return edad

# CÃ¡lculo de estatura
def obtener_estatura():
    estatura = float(input("CuÃ©ntame mÃ¡s de ti, para agregarlo a tu perfil. Â¿CuÃ¡nto mides? DÃ­melo en metros. "))
    metros = int(estatura)
    centimetros = int( (estatura - metros)*100 )
    return (metros, centimetros)
# Cantidad de amigos
def obtener_amigos():
    num_amigos = int(input("Muy bien. Finalmente, Cuéntame cuantos amigos tienes. "))
    return num_amigos
def mostrar_perfil(nombre,edad,metros,centimetros,num_amigos):#Con los datos recolectados escribimos en pantalla un texto que resuma los datos que hemos obtenido
    print()
    print(f"Muy bien, {nombre}. Entonces podemos crear un perfil con estos datos.")
    print("--------------------------------------------------")
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad} años")
    print(f"Estatura: {metros} metros y {centimetros} centímetros")
    print(f"Amigos: {num_amigos}")
    print("--------------------------------------------------")
    print(nombre,"Gracias por la información. Esperamos que disfrutes con Mi Red")
    print()

#Esta opcion permite entrar al ciclo. Solo interesa que no sea 0.
mostrar_bienvenida()
nombre = obtener_nombre()
print()
print(f"Hola{nombre}, bienvenido a Mi red")
edad=obtener_edad()
(metros,centimetros)=obtener_estatura()
num_amigos= obtener_amigos()
mostrar_perfil(nombre,edad,metros,centimetros,num_amigos)

opcion = 1
while opcion != 0:
    print("Acciones disponibles:")
    print("  1. Escribir un mensaje público")
    print("  2. Escribir un mensaje solo a algunos amigos")
    print("  3. Mostrar los datos de perfil")
    print("  4. Actualizar el perfil de usuario")
    print("  0. Salir")
    opcion = int(input("Ingresa una opción: "))

    #CÃ³digo para la opción 1. Publicar un mensaje.
    if opcion == 1:
        mensaje = input("Ahora vamos a publicar un mensaje. ¿Qué piensas hoy? ")
        print()
        print("--------------------------------------------------")
        print(nombre, "dice:", mensaje)
        print("--------------------------------------------------")

    #CÃ³digo para la opción 2. Publicar un mensajes a un grupo de personas.
    elif opcion == 2:
        mensaje = input("Ahora vamos a publicar un mensaje a un grupo de amigos. ¿Qué quieres decirles? ")
        print()
        for i in range(num_amigos):
            nombre_amigo = input("Ingresa el nombre de tu amigo o amiga: ")
            print("--------------------------------------------------")
            print(nombre, "dice:", "@"+nombre_amigo, mensaje)
            print("--------------------------------------------------")

    #CÃ³digo para la opción 3. Publicar los datos del perfil del usuario.
    elif opcion == 3:
        print("--------------------------------------------------")
        print("Nombre:   ", nombre)
        print("Edad:     ", edad, "años")
        print("Estatura: ", estatura_m, "m y ", estatura_cm, "centímetros")
        print("Amigos:   ", num_amigos)
        print("--------------------------------------------------")

    #CÃ³digo para la opción 4. Actualizar los datos del perfil del usuario.
    elif opcion == 4:
        #Repetimos el cÃ³digo para solicitar datos
        # Solicitud de nombre
        nombre = input("Para empezar, dime como te llamas. ")
        print()
        print("Hola ", nombre, ", bienvenido a Mi Red")
        print()

        # CÃ¡lculo de edad
        agno = int(input("Para preparar tu perfil, dime en qué año naciste. "))
        edad = 2017-agno-1
        print()

        # CÃ¡lculo de estatura
        estatura = float(input("Cuéntame más de ti, para agregarlo a tu perfil. ¿Cuánto mides? Dímelo en metros. "))
        estatura_m = int(estatura)
        estatura_cm = int( (estatura - estatura_m)*100 )

        # Cantidad de amigos
        num_amigos = int(input("Muy bien. Finalmente, cuéntame cuantos amigos tienes. "))

        print()
        print("Muy bien,", nombre, ". Entonces podemos crear un perfil con estos datos.")
        # Repetimos el cÃ³digo para mostrar los datos del usuario.
        print("--------------------------------------------------")
        print("Nombre:  ", nombre)
        print("Edad:    ", edad, "años")
        print("Estatura:", estatura_m, "metros y", estatura_cm, "centímetros")
        print("Amigos:  ", num_amigos)
        print("--------------------------------------------------")
        print()

    #CÃ³digo para la opción 0. Salir.
    elif opcion == 0:
        print("Has decidido salir.")

    #CÃ³digo para la opción que no coincida con ninguna anterior.
    else:
        print("No conozco la opción que has ingresado. IntÃ©ntalo otra vez.")

print()
print("Gracias por usar Mi Red. Â¡Hasta pronto!")
print()

#Si pruebas este cÃ³digo, verÃ¡s que funciona correctamente, pero nuestro programa ahora es bastante largo.
#Casi 140 lÃ­neas.
#Esto en sÃ­ no es malo. Sin embargo, si le pones atenciÃ³n, verÃ¡s que hay cÃ³digo que hemos tenido
#que repetir completamente. Por ejemplo, el cÃ³digo para mostrar el perfil de un usuario estÃ¡ escrito tres veces.
#Si ahora queremos agregar un nuevo dato del usuario, por ejemplo, el paÃ­s en que vive, debemos modificar
#al menos tres partes distintas del programa.
#Esto lo podemos hacer, talvez sin cometer errores, en un programa pequeÃ±o como Ã©ste.
#Pero en programas más grandes, es muy fÃ¡cil que nos olvidemos de actualizar una parte del cÃ³digo,
#o que no recordemos todas las partes que hay que modificar.

#Cuando tenemos instrucciones que se repiten tantas veces en distintas partes del programa,
# es una indicaciÃ³n de que talvez necesitamos agregar funciones.

#Te invitamos a pensar en al menos 3 alternativas o funcionalidades de este cÃ³digo
#que podrÃ­an convertirse en una funciÃ³n.