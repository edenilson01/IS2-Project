from sys import path as path
path.append('./')
from app.models.connection_model import DbConnectionModel

class UsuarioRolModel(DbConnectionModel):
    INSERT_ROL_USUARIO_STMT = 'INSERT INTO usuarios_roles(id_rol, username, inicio, fin) VALUES(%s, %s, %s, %s)'
    UPDATE_INI_ROL_USUARIO_STMT = 'UPDATE usuarios_roles SET inicio = %s WHERE id_rol = %s and username = %s'
    UPDATE_FIN_ROL_USUARIO_STMT = 'UPDATE usuarios_roles SET fin = %s WHERE id_rol = %s and username = %s'
    DELETE_ROL_USUARIO_STMT = 'DELETE FROM usuarios_roles WHERE id_rol = %s and username = %s'
    CONSULT_INI_ROL_USUARIO_STMT = 'SELECT inicio FROM usuarios_roles WHERE id_rol = %s and username = %s'
    CONSULT_FIN_ROL_USUARIO_STMT = 'SELECT fin FROM usuarios_roles WHERE id_rol = %s and username = %s'

    def insert_rol_usuario(self, id_rol, username, inicio, fin):
        try:
            super().execute_sql_stmt(self.INSERT_ROL_USUARIO_STMT, (id_rol, username, inicio, fin))
        except Exception as e:
            raise e
    
    def update_fecha_inicio(self, fecha_inicio, id_rol, username):
        try:
            super().execute_sql_stmt(self.UPDATE_INI_ROL_USUARIO_STMT, (fecha_inicio, id_rol, username))
        except Exception as e:
            raise e
    
    def update_fecha_fin(self, fecha_fin, id_rol, username):
        try:
            super().execute_sql_stmt(self.UPDATE_FIN_ROL_USUARIO_STMT, (fecha_fin, id_rol, username))
        except Exception as e:
            raise e
    
    def consult_fecha_inicio(self, id_rol, username):
        try:
            fecha_inicio = super().execute_sql_stmt(self.CONSULT_INI_ROL_USUARIO_STMT, (id_rol, username), True)
            if len(fecha_inicio) == 0:
                return None
            return fecha_inicio[0][0] #VER
        except Exception as e:
            raise e
    
    def consult_fecha_fin(self, id_rol, username):
        try:
            fecha_fin = super().execute_sql_stmt(self.CONSULT_FIN_ROL_USUARIO_STMT, (id_rol, username), True)
            if len(fecha_fin) == 0:
                return None
            return fecha_fin[0][0] #VER
        except Exception as e:
            raise e
    
    def delete_rol_usuario(self, id_rol, username):
        try:
            super().execute_sql_stmt(self.DELETE_ROL_USUARIO_STMT, (id_rol, username))
        except Exception as e:
            raise e
