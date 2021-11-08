class Usuario:
    def __init__(self,Username,Nombre,Genero,correo,Password):
        self.Username = Username
        self.Nombre = Nombre
        self.correo = correo
        self.Genero = Genero
        self.Password = Password
    #Getter
    def getNombre(self):
        return self.Nombre
    def getGenero(self):
        return self.Genero
    def getcorreo(self):
        return self.correo
    def getUsername(self):
        return self.Username
    def getPassword(self):
        return self.Password
    #Setter
    def setGenero(self, Genero):
        self.Genero = Genero
    def setNombre(self, Nombre):
        self.Nombre = Nombre
    def setCorreo(self, correo):
        self.correo = correo
    def setUsername(self, Username):
        self.Username = Username
    def setEdad(self, Password):
        self.Password = Password     