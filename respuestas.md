
El muro de un usuario, se guarda en una lista de strings.


Las relaciones entre amigos en este programa pueden ser unidireccionales. Esto significa que si A es amigo de B, no necesariamente B es también amigo de A


En el programa presentado es posible que un usuario escriba el nombre de un amigo dos veces.


El archivo original no permite que la lista de amigos de un usuario cambie durante la ejecución del programa.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

def agregar_amigo(lista_amigos, nuevo_amigo):
  lista_amigos.extend([nuevo_amigo])

def agregar_amigo(lista_amigos, nuevo_amigo):
  lista_amigos.append(nuevo_amigo)

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

def mostrar_estados_amigos(lista_amigos):
  for amigo in lista_amigos:
    archivo = open(amigo+".user", "r")
    for i in range(7):
      linea = archivo.readline().rstrip()
    print(amigo+":", linea)
    archivo.close()