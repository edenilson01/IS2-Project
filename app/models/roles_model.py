from sys import path as path
path.append('./')
from app.models.connection_model import DbConnectionModel

class RolesModel(DbConnectionModel):
    INSERT_ROL_STMT = 'INSERT INTO roles(nombre, descripcion) VALUES (%s, %s)'
    CONSULT_LAST_ROL = 'SELECT MAX(id_rol) FROM roles'
    CONSULT_ROL_STMT = 'SELECT * FROM roles'
    CONSULT_ROL_STMT_ = 'SELECT id_rol FROM roles WHERE nombre = %s'
    UPDATE_NOMBRE_STMT = 'UPDATE roles SET nombre = %s WHERE id_rol = %s'
    UPDATE_DESC_STMT = 'UPDATE roles SET descripcion = %s WHERE id_rol = %s'
    DELETE_ROL_STMT = 'DELETE FROM roles WHERE id_rol = %s'

    def insert_rol(self, nombre, descripcion):
        try:
            super().execute_sql_stmt(self.INSERT_ROL_STMT, (nombre, descripcion))
            id_rol = super().execute_sql_stmt(self.CONSULT_LAST_ROL, '', True)

            if len(id_rol) == 0:
                return None
            return id_rol[0][0]
        except Exception as e:
            raise e
        
    def consult_roles(self):
        try:
            roles = super().execute_sql_stmt(self.CONSULT_ROL_STMT, '', True)
            if len(roles) == 0:
                return None
            return roles
        except Exception as e:
            raise e

    def consult_roles2(self, nombre):
        try:
            roles = super().execute_sql_stmt(self.CONSULT_ROL_STMT_, (nombre))
            if len(roles) == 0:
                return None
            return roles
        except Exception as e:
            raise e

    def update_nombre(self, nombre, id_rol):
        try:
            super().execute_sql_stmt(self.UPDATE_NOMBRE_STMT, (nombre, id_rol))
        except Exception as e:
            raise e
    
    def update_descripcion(self, descripcion, id_rol):
        try:
            super().execute_sql_stmt(self.UPDATE_DESC_STMT, (descripcion, id_rol))
        except Exception as e:
            raise e
    
    def delete_rol(self, id_rol):
        try:
            super().execute_sql_stmt(self.DELETE_ROL_STMT, [id_rol])
        except Exception as e:
            raise e