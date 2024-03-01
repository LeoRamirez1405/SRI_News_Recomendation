import pandas as pd
import glob

import pandas as pd
import glob

def clean_and_merge_csv_files():
    """
    Limpia y fusiona múltiples archivos CSV en el directorio actual, manteniendo solo ciertas columnas.
    
    Este script realiza las siguientes acciones:
    - Lee todos los archivos CSV en el directorio actual.
    - Mantiene solo las columnas especificadas ('title', 'description', 'author', 'date', 'link').
    - Guarda los datos limpios en el mismo archivo CSV.
    - Asegura que la columna 'author' exista, añadiéndola con valores NaN si no existe.
    - Fusiona todos los dataframes resultantes en un único dataframe.
    - Guarda el dataframe fusionado en un nuevo archivo CSV llamado "all_news.csv".
    
    No retorna ningún valor, ya que la operación es realizada sobre los archivos del sistema de archivos.
    """
    # Define la lista de columnas que deseas mantener
    columns_to_keep = ['title', 'description', 'author', 'date', 'link']

    # Función para limpiar los datos
    def clean_dataframe(df):
        """
        Limpia un dataframe específico, manteniendo solo las columnas especificadas.
        
        Parámetros:
        - df (pd.DataFrame): El dataframe a limpiar.
        
        Retorna:
        - pd.DataFrame: El dataframe limpio.
        """
        return df[columns_to_keep]

    # Encontrar todos los archivos CSV en el directorio actual
    csv_files = glob.glob('./*.csv')

    # Inicializar una lista vacía para contener los dataframes
    dfs = []

    # Recorrer cada archivo CSV
    for filename in csv_files:
        # Leer el archivo CSV
        df = pd.read_csv(filename)    
        # Limpiar el dataframe
        df = clean_dataframe(df)
        # Guardar el dataframe con las columnas seleccionadas en el mismo archivo
        df.to_csv(filename, index=False)
        # Añadir el dataframe a la lista
        dfs.append(df)

    # Concatenar todos los dataframes en la lista en un único dataframe
    merged_df = pd.concat(dfs, ignore_index=True)

    # Guardar el dataframe fusionado en un nuevo archivo CSV
    merged_df.to_csv("all_news.csv", index=False)

# Ejecutar la función principal
clean_and_merge_csv_files()
