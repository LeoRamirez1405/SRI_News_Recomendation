import pandas
import prepro
from class_News import News
from sklearn.metrics.pairwise import cosine_similarity


def query_result(query,loaded_matrix,csvpath,vectorizador,cantDocs_to_return= 0,presition = 0.05):

    df = pandas.read_csv(csvpath)
    # Tokenización y preprocesamiento de la consulta
    query_tokens = prepro.preprocess_documents([query])[0]
    qvector = vectorizador.transform(query_tokens)

    # Calcular las similitudes del coseno entre la consulta y los documentos
    similarity_scores = cosine_similarity(qvector,loaded_matrix)[0]

    similarity_scores = {i: score for i, score in enumerate(similarity_scores)}
    diccionario_ordenado = dict(sorted(similarity_scores.items(), key=lambda item: item[1],reverse = True))
    diccionario_ordenado = {k: v for k, v in diccionario_ordenado.items() if v >  presition}
    
    if cantDocs_to_return > 0:
        # Convertir el diccionario ordenado en una lista de tuplas para poder indexarlo
        lista_ordenada = list(diccionario_ordenado.items())
        # Obtener los primeros 'cantDocs_to_return' elementos de la lista
        diccionario_ordenado = dict(lista_ordenada[:cantDocs_to_return])

    documents = []
    for score in diccionario_ordenado:
        index = score
        title = df.loc[index, 'title']
        try:
            author = df.loc[index, 'author']
        except:
            author = 'Unknown'
        try:
            date = df.loc[index, 'date']
        except:
            date = 'Unknown'
        summary = df.loc[index, 'description']
        url = df.loc[index, 'link']

        news_item = News(title, author, date, summary, url)
        documents.append(news_item)
    return documents

