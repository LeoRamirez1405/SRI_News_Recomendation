class News:
    def __init__(self, title, author, date, summary, url):
        self.title = title
        self.author = author
        self.date = date
        self.summary = summary
        self.url = url

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_author(self):
        return self.author

    def set_author(self, author):
        self.author = author

    def get_date(self):
        return self.date

    def set_date(self, date):
        self.date = date

    def get_summary(self):
        return self.summary

    def set_summary(self, summary):
        self.summary = summary

    def get_url(self):
        return self.url

    def set_url(self, url):
        self.url = url
    
    def print(self):
        print("Title: ",self.get_title())
        print("Author: ",self.author)
        print("Date: ",self.date)
        print("Summary: ",self.get_summary())
        print("URL: ",self.get_url())