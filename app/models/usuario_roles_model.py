from sys import path as path
path.append('./')
from datetime import datetime
from app.models.connection_model import DbConnectionModel

class UsuarioRolModel(DbConnectionModel):
    INSERT_ROL_USUARIO_STMT = 'INSERT INTO usuarios_roles(id_rol, username, inicio, fin) VALUES(%s, %s, %s, %s)'
    UPDATE_FIN_ROL_USUARIO_STMT = 'UPDATE usuarios_roles SET fin = %s WHERE id_rol = %s and username = %s'
    DELETE_ROL_USUARIO_STMT = 'DELETE FROM usuarios_roles WHERE id_rol = %s and username = %s'
    CONSULT_IDS_ROL_USUARIO_STMT = 'SELECT id_rol FROM usuarios_roles WHERE username = %s'
    CONSULT_ROL_USER_STMT = 'SELECT id_rol FROM usuarios_roles WHERE username = %s AND id_rol = %s'
    DELETE_ROLES_USUARIO_STMT = 'DELETE FROM usuarios_roles WHERE username = %s'

    def consult_rol_user(self, username, id_rol):
        try:
            ids = super().execute_sql_stmt(self.CONSULT_ROL_USER_STMT, (username, id_rol), True)
            if len(ids) == 0:
                return None
            return ids
        except Exception as e:
            raise e
    
    def consult_id_roles(self, username):
        try:
            ids = super().execute_sql_stmt(self.CONSULT_IDS_ROL_USUARIO_STMT, [username], True)
            if len(ids) == 0:
                return None
            return ids
        except Exception as e:
            raise e

    def insert_rol_usuario(self, id_rol, username, inicio, fin):
        try:
            super().execute_sql_stmt(self.INSERT_ROL_USUARIO_STMT, (id_rol, username, inicio, fin))
        except Exception as e:
            raise e

    def insert_rol_usuario2(self, id_rol, username):
        inicio = datetime.now()
        fin = None
        try:
            super().execute_sql_stmt(self.INSERT_ROL_USUARIO_STMT, (id_rol, username, inicio, fin))
        except Exception as e:
            raise e
    
    def update_fecha_fin(self, fecha_fin, id_rol, username):
        try:
            super().execute_sql_stmt(self.UPDATE_FIN_ROL_USUARIO_STMT, (fecha_fin, id_rol, username))
        except Exception as e:
            raise e
    
    def delete_rol_usuario(self, id_rol, username):
        try:
            super().execute_sql_stmt(self.DELETE_ROL_USUARIO_STMT, (id_rol, username))
        except Exception as e:
            raise e
    
    def delete_roles_usuario(self, username):
        try:
            super().execute_sql_stmt(self.DELETE_ROLES_USUARIO_STMT, [username])
        except Exception as e:
            raise e
