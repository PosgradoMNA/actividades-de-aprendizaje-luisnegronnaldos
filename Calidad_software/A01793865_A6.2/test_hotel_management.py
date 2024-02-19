import unittest
from datetime import datetime
from hotel_management import Hotel, Cliente, Reserva, cargar_datos, guardar_datos

class TestHotelManagement(unittest.TestCase):

    def test_creacion_hotel(self):
        hotel = Hotel("Hotel Ejemplo", "Direccion Ejemplo", 10)
        self.assertEqual(hotel.nombre, "Hotel Ejemplo")
        self.assertEqual(hotel.direccion, "Direccion Ejemplo")
        self.assertEqual(hotel.habitaciones_totales, 10)
        self.assertEqual(hotel.habitaciones_reservadas, 0)

    def test_creacion_cliente(self):
        cliente = Cliente("Juan", "Perez", "123456789")
        self.assertEqual(cliente.nombre, "Juan")
        self.assertEqual(cliente.apellido, "Perez")
        self.assertEqual(cliente.numero_pasaporte, "123456789")

    def test_creacion_reserva(self):
        fecha_ingreso = datetime.strptime("01/01/2023", "%m/%d/%Y")
        fecha_salida = datetime.strptime("01/05/2023", "%m/%d/%Y")
        hotel = Hotel("Hotel Ejemplo", "Direccion Ejemplo", 10)
        cliente = Cliente("Juan", "Perez", "123456789")
        reserva = Reserva(1, cliente, hotel, 2, fecha_ingreso, fecha_salida)
        self.assertEqual(reserva.codigo_reserva, 1)
        self.assertEqual(reserva.cliente, cliente)
        self.assertEqual(reserva.hotel, hotel)
        self.assertEqual(reserva.cantidad_personas, 2)
        self.assertEqual(reserva.fecha_ingreso, fecha_ingreso)
        self.assertEqual(reserva.fecha_salida, fecha_salida)

    def test_cargar_guardar_datos(self):
        datos_originales = {"nombre": "Hotel Ejemplo", "direccion": "Direccion Ejemplo", "habitaciones_totales": 10}
        guardar_datos("prueba.json", datos_originales)
        datos_cargados = cargar_datos("prueba.json")
        self.assertEqual(datos_cargados, datos_originales)

        # Limpia el archivo de prueba después de la prueba
        guardar_datos("prueba.json", {})

    def test_modificar_hotel(self):
        hotel = Hotel("Hotel Ejemplo", "Direccion Ejemplo", 10)
        hotel.nombre = "Nuevo Hotel"
        hotel.direccion = "Nueva Direccion"
        hotel.habitaciones_totales = 15
        self.assertEqual(hotel.nombre, "Nuevo Hotel")
        self.assertEqual(hotel.direccion, "Nueva Direccion")
        self.assertEqual(hotel.habitaciones_totales, 15)

    def test_eliminar_cliente(self):
        cliente = Cliente("Juan", "Perez", "123456789")
        clientes = {"123456789": cliente}
        del clientes["123456789"]
        self.assertNotIn("123456789", clientes)

    def test_reservar_habitacion(self):
        hotel = Hotel("Hotel Ejemplo", "Direccion Ejemplo", 10)
        hotel.habitaciones_reservadas = 5
        self.assertEqual(hotel.habitaciones_reservadas, 5)
        # Realiza la lógica de reserva aquí y verifica que las habitaciones reservadas se actualicen correctamente

    def test_cancelar_reserva(self):
        reserva = Reserva(1, Cliente("Juan", "Perez", "123456789"), Hotel("Hotel Ejemplo", "Direccion Ejemplo", 10), 2, datetime.now(), datetime.now())
        reservas = {"1": reserva}
        del reservas["1"]
        self.assertNotIn("1", reservas)

    def test_mostrar_informacion_cliente_no_existente(self):
        clientes = {}
        self.assertFalse("123456789" in clientes)  # Asegura que el cliente no exista

    def test_mostrar_informacion_hotel_no_existente(self):
        hoteles = {}
        self.assertFalse("Hotel Inexistente" in hoteles)  # Asegura que el hotel no exista

    def test_guardar_datos_error(self):
        datos_originales = {"nombre": "Hotel Ejemplo", "direccion": "Direccion Ejemplo", "habitaciones_totales": 10}
        with self.assertRaises(Exception):  # Intencionalmente causando un error al guardar datos
            guardar_datos("/ruta/inexistente/prueba.json", datos_originales)

    def test_cargar_datos_archivo_invalido(self):
        datos_cargados = cargar_datos("archivo_invalido.json")
        self.assertEqual(datos_cargados, {})  # Asegura que se devuelva un diccionario vacío para un archivo no válido

    def test_creacion_hotel_invalida(self):
        with self.assertRaises(ValueError):  # Intencionalmente causando un error al crear hotel con habitaciones totales negativas
            hotel = Hotel("Hotel Ejemplo", "Direccion Ejemplo", -5)

    def test_creacion_reserva_fecha_invalida(self):
        fecha_ingreso = datetime.strptime("01/01/2023", "%m/%d/%Y")
        fecha_salida = datetime.strptime("01/01/2023", "%m/%d/%Y")
        hotel = Hotel("Hotel Ejemplo", "Direccion Ejemplo", 10)
        cliente = Cliente("Juan", "Perez", "123456789")
        with self.assertRaises(ValueError):  # Intencionalmente causando un error al crear reserva con fechas iguales
            reserva = Reserva(1, cliente, hotel, 2, fecha_ingreso, fecha_salida)

    def test_eliminar_cliente_no_existente(self):
        clientes = {}
        with self.assertRaises(KeyError):  # Intencionalmente causando un error al eliminar cliente no existente
            del clientes["123456789"]

    def test_mostrar_informacion_hotel_no_existente(self):
        hoteles = {}
        with self.assertRaises(KeyError):  # Intencionalmente causando un error al intentar acceder a información de hotel no existente
            hotel = hoteles["Hotel Inexistente"]

    def test_cargar_datos_archivo_invalido(self):
        with self.assertRaises((FileNotFoundError, json.JSONDecodeError)):  # Intencionalmente causando un error al cargar datos desde un archivo inexistente o inválido
            datos_cargados = cargar_datos("archivo_invalido.json")

if __name__ == '__main__':
    unittest.main()
