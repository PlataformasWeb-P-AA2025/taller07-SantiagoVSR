from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from genera_tablas import Club, Jugador
from configuracion import cadena_base_datos

# Crear conexión a la base de datos
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Diccionario para mapear el nombre del club al objeto Club
clubes_dic = {}

# Leer e insertar datos de Club
with open("data/datos_clubs.txt", "r", encoding="utf-8") as archivo_clubs:
    for linea in archivo_clubs:
        nombre, deporte, fundacion = linea.strip().split(";")
        club = Club(nombre=nombre, deporte=deporte, fundacion=int(fundacion))
        session.add(club)
        clubes_dic[nombre] = club

# Confirmar inserción de clubes
session.commit()

# Leer e insertar datos de Jugador
with open("data/datos_jugadores.txt", "r", encoding="utf-8") as archivo_jugadores:
    for linea in archivo_jugadores:
        nombre, dorsal, posicion, nombre_club = linea.strip().split(";")
        club = clubes_dic[nombre_club]  # Asumimos que el club siempre existe
        jugador = Jugador(
            nombre=nombre,
            dorsal=int(dorsal),
            posicion=posicion,
            club=club
        )
        session.add(jugador)

# Confirmar inserción de jugadores
session.commit()
