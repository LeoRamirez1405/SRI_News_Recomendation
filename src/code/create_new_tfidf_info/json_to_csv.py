import os
import pandas as pd

def convert_json_to_csv_in_directory():
    """
    Convierte todos los archivos JSON en el directorio de trabajo actual a archivos CSV.
    
    Este script recorre todos los archivos en el directorio de trabajo actual y, para cada archivo con extensión .json,
    lee el contenido del archivo JSON en un DataFrame de pandas y luego guarda este DataFrame como un archivo CSV en el
    mismo directorio. El nombre del archivo CSV resultante tiene la misma base que el archivo JSON original, pero con
    la extensión cambiada a .csv.
    
    No retorna ningún valor, ya que la operación es realizada sobre los archivos del sistema de archivos.
    """
    # Obtén el directorio de trabajo actual
    current_directory = os.getcwd()

    # Itera sobre todos los archivos en el directorio actual
    for filename in os.listdir(current_directory):
        # Verifica si el archivo tiene una extensión .json
        if filename.endswith(".json"):
            # Construye la ruta completa del archivo
            json_file_path = os.path.join(current_directory, filename)
            
            # Lee el archivo JSON en un DataFrame de pandas
            df = pd.read_json(json_file_path)
            
            # Construye el nombre del archivo CSV reemplazando la extensión .json con .csv
            csv_file_name = filename.replace(".json", ".csv")
            csv_file_path = os.path.join(current_directory, csv_file_name)
            
            # Escribe el DataFrame en un archivo CSV
            df.to_csv(csv_file_path, index=False)

    print("Conversion completed.")

# Ejecuta la función principal
convert_json_to_csv_in_directory()
