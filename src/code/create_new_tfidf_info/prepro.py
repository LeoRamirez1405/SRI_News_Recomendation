import nltk
import spacy
import gensim

nlp = spacy.load("en_core_web_sm")

def tokenization_spacy(texts):
    """
    Realiza la tokenización de una lista de textos utilizando spaCy.
    
    Parámetros:
    - texts (list): Lista de cadenas de texto para tokenizar.
    
    Retorna:
    - list: Lista de listas de tokens.
    """
    return [[token for token in nlp(doc)] for doc in texts]

def remove_noise_spacy(tokenized_docs):
    """
    Elimina tokens no alfabéticos de una lista de listas de tokens.
    
    Parámetros:
    - tokenized_docs (list): Lista de listas de tokens.
    
    Retorna:
    - list: Lista de listas de tokens sin caracteres no alfabéticos.
    """
    return [[token for token in doc if token.is_alpha] for doc in tokenized_docs]

def remove_stopwords_spacy(tokenized_docs):
    """
    Elimina las palabras vacías (stop words) de una lista de listas de tokens.
    
    Parámetros:
    - tokenized_docs (list): Lista de listas de tokens.
    
    Retorna:
    - list: Lista de listas de tokens sin palabras vacías.
    """
    stopwords = spacy.lang.en.stop_words.STOP_WORDS
    return [
        [token for token in doc if token.text not in stopwords] for doc in tokenized_docs
    ]

def morphological_reduction_spacy(tokenized_docs, use_lemmatization=True):
    """
    Realiza la reducción morfológica en una lista de listas de tokens, aplicando lematización o estemming.
    
    Parámetros:
    - tokenized_docs (list): Lista de listas de tokens.
    - use_lemmatization (bool): Indica si se debe usar lematización (True) o estemming (False). Por defecto, True.
    
    Retorna:
    - list: Lista de listas de tokens con reducción morfológica aplicada.
    """
    stemmer = nltk.stem.PorterStemmer()
    return [
        [token.lemma_ if use_lemmatization else stemmer.stem(token.text) for token in doc]
        for doc in tokenized_docs
    ]

def preprocess_documents(documents):  
    """
    Preprocesa una lista de documentos aplicando tokenización, eliminación de ruido, eliminación de palabras vacías y reducción morfológica.
    
    Parámetros:
    - documents (list): Lista de cadenas de texto a preprocesar.
    
    Retorna:
    - list: Lista de listas de tokens preprocesados.
    """
    # Tokenización
    tokenized_docs = tokenization_spacy(documents)

    # Eliminación de ruido (solo tokens alfabéticos)
    tokenized_docs = remove_noise_spacy(tokenized_docs)
    
    # Eliminación de palabras vacías
    tokenized_docs = remove_stopwords_spacy(tokenized_docs)
    
    # Reducción Morfológica
    tokenized_docs = morphological_reduction_spacy(tokenized_docs)

    return tokenized_docs
