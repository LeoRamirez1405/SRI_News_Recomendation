import pandas
import prepro
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

def load_mat(name):
    """
    Carga una matriz TF-IDF previamente guardada en un archivo .joblib.
    
    Parámetros:
    - name (str): Nombre del archivo .joblib que contiene la matriz TF-IDF.
    
    Retorna:
    - np.array: Matriz TF-IDF cargada.
    """
    tfidf_matrix = joblib.load(name)
    return tfidf_matrix

def load_vec(name):
    """
    Carga un vectorizador previamente guardado en un archivo .joblib.
    
    Parámetros:
    - name (str): Nombre del archivo .joblib que contiene el vectorizador.
    
    Retorna:
    - TfidfVectorizer: Vectorizador cargado.
    """
    vectorizer = joblib.load(name)
    return vectorizer

def save_info_to_Joblib(csvpath, cantDocs):
    """
    Preprocesa los documentos de un archivo CSV, calcula la matriz TF-IDF y guarda tanto la matriz como el vectorizador en archivos .joblib.
    
    Parámetros:
    - csvpath (str): Ruta al archivo CSV que contiene los documentos.
    - cantDocs (int): Número de documentos a procesar desde el archivo CSV.
    
    Retorna:
    - TfidfVectorizer: Vectorizador utilizado para calcular la matriz TF-IDF.
    """
    # Leer el archivo CSV en un DataFrame de pandas
    df = pandas.read_csv(csvpath)

    # Aquí cargamos los documentos
    documents = [doc['title'] + " " + doc['description'] for _, doc in df.iterrows()]
    documents = documents[:cantDocs]

    # Preprocesamiento de los documentos
    preprocessed_docs = prepro.preprocess_documents(documents)

    # Convertir cada lista de tokens en una cadena única
    preprocessed_docs = [' '.join(doc) for doc in preprocessed_docs]

    # Crear el vectorizador y calcular la matriz TF-IDF
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(preprocessed_docs)

    joblib.dump(tfidf_vectorizer, 'vectorizer.joblib')
    joblib.dump(tfidf_matrix, 'matrix.joblib')
    
    return tfidf_vectorizer
