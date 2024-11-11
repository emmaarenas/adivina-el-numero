# Programa Adivina el Número

## Características

🔹 Este repositorio es ideal para explorar de una manera simple las capacidades de Python en el desarrollo de juegos interactivos y en el análisis de datos. El programa permite jugar en modo solitario o en un modo para dos jugadores; incluyendo diferentes dificultades de juego y pistas.

🔹 El juego ofrece estadísticas detalladas de cada partida, que se almacenan automáticamente en un archivo Excel (gracias a la librería **Openpyxl**). Esta función permite a los jugadores analizar su rendimiento a través de datos como: resultado, modo de juego, nivel de dificultad y cantidad de intentos. Además, el proyecto incluye visualizaciones con **Matplotlib** para interpretar fácilmente el rendimiento de los jugadores y la distribución de dificultades.

## Archivos del proyecto

1. **Adivina_El_Numero.py**
   - Este archivo contiene el programa principal del juego "Adivina el Número".
   - Aquí se maneja la lógica del juego y se llama a las funciones necesarias para su funcionamiento.
   - Este archivo utiliza el módulo `Adivinanza.py` para acceder a las funciones que realizan las operaciones del juego.
   - **Nota**: Para una mejor experiencia visual, es recomendable abrir este archivo en un IDE que soporte códigos ANSI, ya que se han utilizado para mejorar la estética del juego.

2. **Adivinanza.py**
   - Este archivo es el módulo que contiene las funciones esenciales para el juego.
   - Define las funciones que permiten ejecutar la lógica de "Adivina el Número" y gestionar las estadísticas del juego.
   - `Adivina_El_Numero.py` importa este módulo y utiliza sus funciones para que el programa funcione correctamente.

3. **Estadística.xlsx**
   - Este archivo almacena los datos del juego, como el nombre y resultados de cada jugador.
   - Se actualiza automáticamente con cada partida, permitiendo almacenar las estadísticas del juego.
   - En el archivo ya existen algunos datos a modo de ejemplo que he generado.

## Cómo ejecutar el programa

Este proyecto requiere Python y las siguientes bibliotecas:
- `openpyxl`
- `matplotlib`

Para instalar estas dependencias, puedes usar el siguiente comando:
```bash
pip install -r requirements.txt
