from sys import path as path
path.append('./')
from app.models.connection_model import DbConnectionModel

class UserModel(DbConnectionModel):
    SELECT_USER_STMT = 'SELECT password FROM usuarios WHERE username = %s'
    INSERT_USER_STMT = 'INSERT INTO usuarios(username, password, id_persona) VALUES (%s, %s, %s)'
    DELETE_USER_STMT = 'DELETE FROM usuarios WHERE username = %s'
    UPDATE_USER_STMT = 'UPDATE usuarios SET password = %s, correo = %s WHERE username = %s'

    def __init__(self):
        super().__init__()
    
    def insert_user(self, username, password, id_persona):
        try:
            super().execute_sql_stmt(self.INSERT_USER_STMT, (username, password, id_persona))
        except Exception as e:
            raise e

    def consult_password(self, username):
        try:
            password = super().execute_sql_stmt(self.SELECT_USER_STMT, [username], True)
            if len(password) == 0:
                return None
            return password[0][0]
        except Exception as e:
            raise e

    def delete_user(self, username):
        try:
            super().execute_sql_stmt(self.DELETE_USER_STMT, [username])
        except Exception as e:
            raise e
    
    def update_user(self, password, correo, username):
        try:
            super().execute_sql_stmt(self.UPDATE_USER_STMT, (password, correo, username))
        except Exception as e:
            raise e