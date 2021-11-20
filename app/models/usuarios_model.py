from sys import path as path
path.append('./')
from app.models.connection_model import DbConnectionModel

class UserModel(DbConnectionModel):
    SELECT_USER_STMT = 'SELECT * FROM usuarios WHERE estado IS TRUE AND username = %s'
    SELECT_ID_PER_STMT = 'SELECT id_persona FROM usuarios WHERE estado IS TRUE AND username = %s'
    INSERT_USER_STMT = 'INSERT INTO usuarios(username, password, id_persona, correo, estado) VALUES (%s, %s, %s, %s, %s)'
    DELETE_USER_STMT = 'UPDATE usuarios SET estado = FALSE WHERE username = %s'
    UPDATE_USER_STMT = 'UPDATE usuarios SET password = %s, correo = %s WHERE username = %s'
    UPDATE_USER_US_STMT = 'UPDATE us SET username = NULL'
    SELECT_USER_EXISTS_STMT = 'SELECT * FROM usuarios WHERE username = %s'
    SELECT_NAME_STMT = '''select p.primer_nombre || ' ' || p.primer_apellido as nombre
        from usuarios u 
        inner join personas p on p.id_persona = u.id_persona 
        where u.username = %s'''

    def __init__(self):
        super().__init__()

    def consultar_nombre(self, username):
        try:
            nombre = super().execute_sql_stmt(self.SELECT_NAME_STMT, [username], True)
            if len(nombre) == 0:
                return None
            return nombre[0][0]
        except Exception as e:
            raise e
    
    def insert_user(self, username, password, id_persona, correo, estado = True):
        try:
            super().execute_sql_stmt(self.INSERT_USER_STMT, (username, password, id_persona, correo, estado))
        except Exception as e:
            raise e
    
    def consult_id_persona(self, username):
        try:
            id_persona = super().execute_sql_stmt(self.SELECT_ID_PER_STMT, [username], True)
            if len(id_persona) == 0:
                return None
            return id_persona[0][0]
        except Exception as e:
            raise e

    def consult_persona_exists(self, username):
        try:
            users = super().execute_sql_stmt(self.SELECT_USER_EXISTS_STMT, [username], True)
            if len(users) == 0:
                return None
            return users[0]
        except Exception as e:
            raise e
    
    def consult_persona(self, username):
        try:
            users = super().execute_sql_stmt(self.SELECT_USER_STMT, [username], True)
            if len(users) == 0:
                return None
            return users[0]
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