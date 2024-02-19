# codigo hotel_management.py
"programa para gestion un hotel"
import json
from datetime import datetime


class Hotel:
    "define la clase Hotel"
    def __init__(self, nombre, direccion, habitaciones_totales):
        self.nombre = nombre
        self.direccion = direccion
        self.habitaciones_totales = habitaciones_totales
        self.habitaciones_reservadas = 0


class Cliente:
    "define la clase Cliente"
    def __init__(self, nombre, apellido, numero_pasaporte):
        self.nombre = nombre
        self.apellido = apellido
        self.numero_pasaporte = numero_pasaporte


class Reserva:
    "define la clase Reserva"
    codigo_reserva = 1

    def __init__(self, codigo_reserva, cliente, hotel, cantidad_personas,
                 fecha_ingreso, fecha_salida):
        self.codigo_reserva = codigo_reserva
        self.cliente = cliente
        self.hotel = hotel
        self.cantidad_personas = cantidad_personas
        self.fecha_ingreso = datetime.strptime(fecha_ingreso, "%m/%d/%Y")
        self.fecha_salida = datetime.strptime(fecha_salida, "%m/%d/%Y")


def cargar_datos(nombre_archivo):
    """define la forma de carga de datos"""
    try:
        with open(nombre_archivo, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def guardar_datos(nombre_archivo, datos):
    """Define como guardar datos"""
    with open(nombre_archivo, 'w') as file:
        json.dump(datos, file, default=serialize, indent=2)


def serialize(obj):
    """serializa los datos de fecha"""
    if isinstance(obj, datetime):
        return obj.strftime('%Y-%m-%d %H:%M:%S')
    return obj.__dict__


def mostrar_menu():
    "define el menu principal"
    print("1. Hotels")
    print("2. Cliente")
    print("3. Reserva")
    print("0. Salir")


def mostrar_submenu_hotels():
    "define el sub menu hoteles"
    print("a. Crear Hotel")
    print("b. Borrar Hotel")
    print("c. Mostrar información del hotel")
    print("d. Modificar información del hotel")
    print("e. Reservar una habitación")
    print("f. Cancelar una reserva")


def mostrar_submenu_cliente():
    "define el sub menu cliente"
    print("a. Crear cliente")
    print("b. Eliminar un cliente")
    print("c. Mostrar información del cliente")
    print("d. Modificar información del cliente")


def mostrar_submenu_reserva():
    "define el sub menu reserva"
    print("a. Crear una Reserva")
    print("b. Cancelar una Reserva")


def main():
    """ funcion principal"""
    hoteles = cargar_datos("hoteles.json")
    clientes = cargar_datos("clientes.json")
    reservas = cargar_datos("reservas.json")

    while True:
        mostrar_menu()
        opcion_principal = input("Selecciona una opción (0 para salir): ")

        if opcion_principal == "1":
            mostrar_submenu_hotels()
            opcion_hotel = input("Selecciona una opción: ")

            if opcion_hotel == "a":
                nombre = input("Nombre del hotel: ")
                direccion = input("Dirección del hotel: ")
                habitaciones_totales = int(input("Cantidad de habitaciones: "))
                hoteles[nombre] = Hotel(nombre, direccion, habitaciones_totales)

            elif opcion_hotel == "b":
                nombre = input("Nombre del hotel a borrar: ")
                if nombre in hoteles:
                    del hoteles[nombre]
                else:
                    print("El hotel no existe.")

            elif opcion_hotel == "c":
                # Mostrar información del hotel
                nombre = input("Nombre del hotel: ")
                if nombre in hoteles:
                    hotel = hoteles[nombre]
                    print(f"Nombre: {hotel.nombre}")
                    print(f"Dirección: {hotel.direccion}")
                    print(f"Hab. Reservadas: {hotel.habitaciones_reservadas}")
                    print(f"Hab. Disponible: {hotel.habitaciones_totales - hotel.habitaciones_reservadas}")
                else:
                    print("El hotel no existe.")

            elif opcion_hotel == "d":
                # Modificar información del hotel
                nombre = input("Nombre del hotel a modificar: ")
                if nombre in hoteles:
                    hotel = hoteles[nombre]
                    hotel.nombre = input("Nuevo nombre del hotel: ")
                    hotel.direccion = input("Nueva dirección del hotel: ")
                    hotel.habitaciones_totales = int(input("Cantidad de habitaciones: "))
                else:
                    print("El hotel no existe.")

            elif opcion_hotel == "e":
                # Reservar una habitación
                nombre_hotel = input("Nombre del hotel: ")
                if nombre_hotel in hoteles:
                    hotel = hoteles[nombre_hotel]
                    # Implementa la lógica para reservar habitación aquí
                else:
                    print("El hotel no existe.")

            elif opcion_hotel == "f":
                # Cancelar una reserva
                # Implementa la lógica para cancelar una reserva aquí
                pass

        elif opcion_principal == "2":
            mostrar_submenu_cliente()
            opcion_cliente = input("Selecciona una opción: ")

            if opcion_cliente == "a":
                # Crear Cliente
                nombre = input("Nombre del cliente: ")
                apellido = input("Apellido del cliente: ")
                numero_pasaporte = input("Número de pasaporte del cliente: ")
                clientes[numero_pasaporte] = Cliente(nombre, apellido,
                                                     numero_pasaporte)

            elif opcion_cliente == "b":
                # Eliminar un Cliente
                numero_pasaporte = input("Pasaporte del cliente a eliminar: ")
                if numero_pasaporte in clientes:
                    del clientes[numero_pasaporte]
                    print("El cliente eliminado.")
                else:
                    print("El cliente no existe.")

            elif opcion_cliente == "c":
                # Mostrar información del Cliente
                numero_pasaporte = input("Número de pasaporte del cliente: ")
                if numero_pasaporte in clientes:
                    cliente = clientes[numero_pasaporte]
                    print(f"Nombre: {cliente.nombre}")
                    print(f"Apellido: {cliente.apellido}")
                    print(f"Número de pasaporte: {cliente.numero_pasaporte}")
                else:
                    print("El cliente no existe.")

            elif opcion_cliente == "d":
                # Modificar información del Cliente
                numero_pasaporte = input("Pasaporte del cliente a modificar: ")
                if numero_pasaporte in clientes:
                    cliente = clientes[numero_pasaporte]
                    cliente.nombre = input("Nuevo nombre del cliente: ")
                    cliente.apellido = input("Nuevo apellido del cliente: ")
                else:
                    print("El cliente no existe.")

        elif opcion_principal == "3":
            mostrar_submenu_reserva()
            opcion_reserva = input("Selecciona una opción: ")

            if opcion_reserva == "a":
                # Crear una Reserva
                codigo_reserva = input("Ingrese el codigo de reserva: ")
                cliente = input("Nombre del cliente: ")
                hotel = input("Apellido del cliente: ")
                cantidad_personas = input("Cantidad de personas: ")
                fecha_ingreso = input("Fecha de ingreso (MM/DD/YYYY): ")
                fecha_salida = input("Fecha de salida (MM/DD/YYYY): ")
                reservas[codigo_reserva] = Reserva(codigo_reserva, cliente,
                                                   hotel, cantidad_personas,
                                                   fecha_ingreso, fecha_salida)

            elif opcion_reserva == "b":
                # Cancelar una Reserva
                codigo_reserva = input("Número de reserva a cancelar: ")
                if codigo_reserva in reservas:
                    del reservas[codigo_reserva]
                    print("Reserva Eliminada.")
                else:
                    print("Reserva no existe.")

        elif opcion_principal == "0":
            # Salir del programa
            guardar_datos("hoteles.json", hoteles)
            guardar_datos("clientes.json", clientes)
            guardar_datos("reservas.json", reservas)
            break

        else:
            print("Opción no válida. Por favor, elige una opción válida.")


if __name__ == "__main__":
    main()
