from datetime import datetime
import pytest

def obtener_edad():
    agno = int(input("Para preparar tu perfil, dime en qué año naciste. "))
    edad = datetime.now().year - agno - 1
    return edad

def test_obtener_edad():
    # Simulamos la entrada de un año de nacimiento
    birth_year = 1990
    # Obtenemos la edad utilizando la función
    edad = obtener_edad(birth_year)
    # Verificamos si la edad calculada es correcta
    assert edad == datetime.now().year - birth_year - 1
