# BusquedaClima

Este es un programa en Python que permite consultar el clima actual de cualquier ciudad utilizando la API de [WeatherAPI](https://www.weatherapi.com/).

## Características
- Consulta el clima en tiempo real de cualquier ciudad.
- Muestra la temperatura en grados Celsius y Fahrenheit.
- Indica la condición climática actual (soleado, lluvioso, etc.).

## Requisitos
- Python 3.x instalado.
- La librería `requests` (puedes instalarla con `pip install requests`).
- Una clave API de WeatherAPI (puedes obtenerla [aquí](https://www.weatherapi.com/)).

## Instalación y Uso
1. Clona este repositorio o descarga el archivo.
2. Asegúrate de tener la librería `requests` instalada.
3. Reemplaza `TU_API_KEY` en el código con tu clave API.
4. Ejecuta el script:
   ```sh
   python nombre_del_archivo.py
   ```
5. Ingresa el nombre de la ciudad cuando se te pida.

## Ejemplo de Uso
```
Ingresa la ciudad a consultar: Bogotá
Ciudad: Bogotá
Temperatura: 18°C / 64°F
Condición: Parcialmente nublado
```

## Notas
- Si la ciudad no es encontrada, el programa mostrará un mensaje de error.
- Asegúrate de proteger tu clave API antes de subir el código a un repositorio público.

## Autor
- Juan Camilo Muñoz

## Licencia
Este proyecto está bajo la licencia MIT.

