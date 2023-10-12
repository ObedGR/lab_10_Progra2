import mysql.connector

class Libro:
    def __init__(self, Titulo, Autor, Editorial, Paginas, Anio, ISBN):
        self.__Titulo = Titulo
        self.__Autor = Autor
        self.__Editorial = Editorial
        self.__Paginas = Paginas
        self.__Anio = Anio
        self.__ISBN = ISBN
        
    # Getters
    def get_Titulo(self):
        return self.__Titulo

    def get_Autor(self):
        return self.__Autor

    def get_Editorial(self):
        return self.__Editorial

    def get_Paginas(self):
        return self.__Paginas

    def get_Anio(self):
        return self.__Anio

    def get_ISBN(self):
        return self.__ISBN

    # Setters
    def set_Titulo(self, Titulo):
        self.__Titulo = Titulo

    def set_Autor(self, Autor):
        self.__Autor = Autor

    def set_Editorial(self, Editorial):
        self.__Editorial = Editorial

    def set_Paginas(self, Paginas):
        self.__Paginas = Paginas

    def set_Anio(self, Anio):
        self.__Anio = Anio

    def set_ISBN(self, ISBN):
        self.__ISBN = ISBN

class Conexion:
    def __init__(self, host, user, password, db):
        self.__host = host
        self.__user = user
        self.__password = password
        self.__db = db
    
    #Getters
    def get_host(self):
        return self.__host
    
    def get_user(self):
        return self.__user
    
    def get_password(self):
        return self.__password
    
    def get_db(self):
        return self.__db
    
    def conexion(self):
        con = mysql.connector.connect(
            host=self.__host,
            user=self.__user,
            password=self.__password,
            database=self.__db
        )
        return con