import pymysql

class DataBase:
    # Constructor de la clase que permite realizar la conexión a bd
    def __init__(self):
        #se crea variable de conexión a bd con todos los parametros necesarios
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            db='user'
        )

        #se crea variable cursor que se utiliza para la ejecución de consultas bd
        self.cursor = self.connection.cursor()
        print("Conexión establecida correctamente")

    #método buscar usuario, permite realizar la consulta de un usuario en bd
    def select_user(self, documento):
        #se crea consulta bd
        sql = "SELECT documento, nombres, apellidos, ciudad, telefono, email FROM user_management WHERE documento = '{}'".format(
            documento)

        try:
            #se ejecuta la consulta en bd
            self.cursor.execute(sql)
            #se retornan los datos de la consulta
            user = self.cursor.fetchone()

            return user

        except Exception as e:
            raise

    #método que permite realizar la consulta de todos los usuarios en bd
    def select_all(self):
        sql = 'SELECT documento, nombres, apellidos, ciudad, telefono, email FROM user_management'

        try:
            self.cursor.execute(sql)
            users = self.cursor.fetchall()

            return users

        except Exception as e:
            raise

    def update_user(self, documento, nombres, apellidos, ciudad, telefono, email):
        sql = "UPDATE user_management SET nombres='{}',  apellidos='{}', ciudad='{}',  telefono='{}',  email='{}' " \
              "WHERE documento ='{}'".format(nombres, apellidos, ciudad, telefono, email, documento)

        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise

    def delete_user(self, documento):
        sql = "DELETE FROM user_management WHERE documento ='{}'".format(documento)

        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            raise


    def insert_user(self, documento, nombres, apellidos, ciudad, telefono, email):
        sql = "INSERT INTO user_management(documento, nombres, apellidos, ciudad, telefono, email) VALUES" \
              "('{}','{}','{}','{}','{}','{}')".format(documento, nombres, apellidos, ciudad, telefono, email)

        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            raise
