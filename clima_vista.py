import requests  # Importamos la librería requests para hacer peticiones HTTP.

class BusquedaClima:
    def __init__(self):  # Método constructor de la clase
        try:
            # Solicitamos al usuario que ingrese la ciudad que desea consultar
            usuario_busqueda = input("Ingresa la ciudad a la que quieres consultar: ")

            # Construimos la URL de la API con la ciudad ingresada
            self.url_consulta = f"http://api.weatherapi.com/v1/current.json?key=TU_KEY={usuario_busqueda}"

            # Hacemos la petición GET a la API
            respuesta = requests.get(self.url_consulta)

            # Convertimos la respuesta en formato JSON
            peticion_json = respuesta.json()

            # Extraemos los datos de la sección "current" del JSON
            clima_actual = peticion_json["current"]

            # Extraemos la descripción del clima desde "condition"
            condicion = clima_actual["condition"]["text"]

            # Mostramos la ciudad consultada
            print(f"Ciudad: {peticion_json['location']['name']}.")

            # Mostramos la temperatura en grados Celsius y Fahrenheit
            print(f"Temperatura: {clima_actual['temp_c']} °C / {clima_actual['temp_f']} °F.")

            # Mostramos la condición climática
            print(f"Condicion: {condicion}.")

        except Exception as error:
            # Capturamos cualquier error y mostramos un mensaje
            print(f"Error en el programa: {error}.")

# Verificamos si el script se está ejecutando directamente
if __name__ == "__main__":
    buscador = BusquedaClima()  # Creamos una instancia de la clase para ejecutar el programa
