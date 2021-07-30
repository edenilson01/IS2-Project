#modelos para la conexion a las bases de datos
#pueden agregarse mas archivos si es necesario
from contextlib import closing
from os import environ
import psycopg2

class DbConnectionModel:
    DB_CONNECTION_PARMS = "dbname=is2_project user=postgres password=password host=localhost port=5432"

    def __init__(self):
        self.connectiondb = None
        self.cursor = None
    
    def execute_sql_stmt(self, statement, values, is_query=False):
        try:
            result = None
            db_params = self.DB_CONNECTION_PARMS %(environ['USER_DB'], environ['USER_DB_PASSWORD'])
            with closing(psycopg2.connect(db_params)) as connection:
                with closing(connection.cursor()) as cursor:
                    result = cursor.execute(statement, values)
                    if is_query:
                        result = cursor.fetchall()
                    connection.commit()
            return result
        except Exception as e:
            raise e