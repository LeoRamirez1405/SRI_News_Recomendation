class News:
    """
    Clase News representa una noticia con atributos como título, autor, fecha, resumen y URL.
    
    Atributos:
    - title (str): El título de la noticia.
    - author (str): El autor de la noticia.
    - date (str): La fecha de la noticia.
    - summary (str): Un resumen de la noticia.
    - url (str): La URL de la noticia.
    """

    def __init__(self, title, author, date, summary, url):
        """
        Inicializa una nueva instancia de la clase News.
        
        Parámetros:
        - title (str): El título de la noticia.
        - author (str): El autor de la noticia.
        - date (str): La fecha de la noticia.
        - summary (str): Un resumen de la noticia.
        - url (str): La URL de la noticia.
        
        Asegura que todos los parámetros sean cadenas de texto (str) y si no lo son, los convierte a str.
        Si algún parámetro no es una cadena de texto, se asigna una cadena vacía a su atributo correspondiente.
        """
        if not isinstance(title, str):
            self.title = ""
        else:
            self.title = str(title)
        
        if not isinstance(author, str):
            self.author = ""
        else:
            self.author = str(author)
        
        if not isinstance(date, str):
            self.date = ""
        else:
            self.date = str(date)
        
        if not isinstance(summary, str):
            self.summary = ""
        else:
            self.summary = str(summary)
            
        if not isinstance(url, str):
            self.url = ""
        else:
            self.url = str(url)

    def get_title(self):
        """
        Devuelve el título de la noticia.
        
        Retorna:
        - str: El título de la noticia.
        """
        return self.title

    def get_author(self):
        """
        Devuelve el autor de la noticia.
        
        Retorna:
        - str: El autor de la noticia.
        """
        return self.author

    def get_date(self):
        """
        Devuelve la fecha de la noticia.
        
        Retorna:
        - str: La fecha de la noticia.
        """
        return self.date

    def get_summary(self):
        """
        Devuelve un resumen de la noticia.
        
        Retorna:
        - str: Un resumen de la noticia.
        """
        return self.summary

    def get_url(self):
        """
        Devuelve la URL de la noticia.
        
        Retorna:
        - str: La URL de la noticia.
        """
        return self.url

    def print_new(self):
        """
        Imprime la información de la noticia en un formato legible.
        
        Retorna:
        - str: La información de la noticia en formato de texto.
        """
        try:
            title = self.title
        except:
            title = ""

        try:
            author = self.author
        except:
            author = ""

        try:
            date = self.date
        except:
            date = ""
        try:
            desc = self.summary
        except:
            desc = ""

        result = "Título: {} \nAutor: {} \nFecha: {} \nTexto Principal: {}\nURL: {}".format(title, author, date, desc,self.url)
        return result
    
    def serialize(self):
        """
        Serializa la noticia en un diccionario con claves correspondientes a los atributos de la noticia.
        
        Retorna:
        - dict: Un diccionario con la información de la noticia.
        """
        return {
            'title': self.title,
            'author': self.author,
            'date': self.date,
            'summary': self.summary, 
            'url': self.url
        }
