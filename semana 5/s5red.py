
def mostrar_bienvenida():
    print("Bienvenido a ... ")
    print("""
                  _                  __
       ____ ___  (_)  ________  ____/ /
      / __ `__ \/ /  / ___/ _ \/ __  /
     / / / / / / /  / /  /  __/ /_/ /
    /_/ /_/ /_/_/  /_/   \___/\__,_/

    """)


def obtener_nombre():
    nombre = input("Para empezar, dime como te llamas. ").capitalize()
    return nombre


def obtener_edad():
    agno = int(input("Para preparar tu perfil, dime en quÃ© aÃ±o naciste. "))
    return 2023-agno-1


def obtener_estatura():
    estatura = float(input(
        "CuÃ©ntame mÃ¡s de ti, para agregarlo a tu perfil. Â¿CuÃ¡nto mides? DÃ­melo en metros. "))
    metros = int(estatura)
    centimetros = int((estatura - metros)*100)
    return (metros, centimetros)


def obtener_sexo():
    sexo = input(
        "Por favor, ingresa tu sexo (M=Masculino, F=Femenino): ").upper()
    while sexo != 'M' and sexo != 'F':
        sexo = input(
            "Por favor, ingresa tu sexo (M=Masculino, F=Femenino): ").upper()
    return sexo


def obtener_pais():
    pais = input("Indica tu paÃ­s de nacimiento: ").capitalize()
    return pais


def obtener_num_amigos():
    amigos = int(
        input("Muy bien. Finalmente, cuÃ©ntame cuantos amigos tienes. "))
    return amigos


def obtener_datos():
    n = obtener_nombre()
    e = obtener_edad()
    (em, ec) = obtener_estatura()
    na = obtener_num_amigos()
    return (n, e, em, ec, na)


def mostrar_perfil(nombre, edad, estatura_m, estatura_cm, sexo, pais, num_amigos):
    print("--------------------------------------------------")
    print("Nombre:   ", nombre)
    print("Edad:     ", edad, "aÃ±os")
    print("Estatura: ", estatura_m, "m y ", estatura_cm, "centÃ­metros")
    print("Sexo:     ", sexo)
    print("País:    ", pais)
    print("Amigos:   ", num_amigos)
    print("--------------------------------------------------")


def opcion_menu():
    print("Acciones disponibles:")
    print("  1. Escribir un mensaje pÃºblico")
    print("  2. Escribir un mensaje solo a algunos amigos")
    print("  3. Mostrar los datos de perfil")
    print("  4. Actualizar el perfil de usuario")
    print("  0. Salir")
    opcion = int(input("Ingresa una opciÃ³n: "))
    while opcion < 0 or opcion > 4:
        print("No conozco la opciÃ³n que has ingresado. IntÃ©ntalo otra vez.")
        opcion = int(input("Ingresa una opciÃ³n: "))
    return opcion


def obtener_mensaje():
    mensaje = input(
        "Ahora vamos a publicar un mensaje. Â¿QuÃ© piensas hoy? ").capitalize()
    return mensaje


def mostrar_mensaje(origen, destinatario, mensaje):
    print("--------------------------------------------------")
    if destinatario == None:
        print(origen, "dice:", mensaje)
    else:
        print(origen, "dice:", "@"+destinatario, mensaje)
    print("--------------------------------------------------")


def leer_datos_usuario(nombre_archivo):
    with open(nombre_archivo, "r") as archivo_usuario:
        nombre = archivo_usuario.readline().strip()
        edad = int(archivo_usuario.readline().strip())
        estatura = float(archivo_usuario.readline().strip())
        estatura_m = int(estatura)
        estatura_cm = int((estatura-estatura_m)*100)
        sexo = archivo_usuario.readline().strip()
        pais = archivo_usuario.readline().strip()
        num_amigos = archivo_usuario.readline().strip()
        estado = archivo_usuario.readline().strip()
        return nombre, edad, estatura_m, estatura_cm, sexo, pais, num_amigos, estado


def guardar_datos_usuario(archivo, nombre, edad, estatura, sexo, pais, num_amigos, estado):
    archivo_usuario = open(archivo, "w")
    archivo_usuario.write(nombre + "\n")
    archivo_usuario.write(str(edad) + "\n")
    archivo_usuario.write(str(estatura[0] + estatura[1] / 100) + "\n")
    archivo_usuario.write(sexo + "\n")
    archivo_usuario.write(pais + "\n")
    archivo_usuario.write(str(num_amigos) + "\n")
    archivo_usuario.write(estado + "\n")
    archivo_usuario.close()