class News:
    def __init__(self, title, author, date, summary, url):
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
        return self.title

    def get_author(self):
        return self.author

    def get_date(self):
        return self.date

    def get_summary(self):
        return self.summary

   
    def get_url(self):
        return self.url

    def print_new(self):
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
        return {
            'title': self.title,
            'author': self.author,
            'date': self.date,
            'summary': self.summary, 
            'url': self.url
        }