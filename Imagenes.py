class Imagen:
    def __init__(self,url,date,category):
        self.url= url
        self.date = date
        self.category = category

    def getUrl(self):
        return self.url
    def getDate(self):
        return self.date
    def getCategory(self):
        return self.category

    def setUrl(self,url):
        self.url=url
    def setDate(self,date):
        self.date=date
    def setCategory(self,category):
        self.category=category

