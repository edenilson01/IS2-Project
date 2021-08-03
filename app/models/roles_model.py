from sys import path as path
path.append('./')
from app.models.connection_model import DbConnectionModel

class RolesModel(DbConnectionModel):
    INSERT_ROL_STMT = 'INSERT INTO roles(nombre, descripcion) VALUES (%s, %s)'
    CONSULT_ROL_STMT = 'SELECT * FROM roles WHERE id_rol = %s'
    UPDATE_NOMBRE_STMT = 'UPDATE roles SET nombre = %s WHERE id_rol = %s'
    UPDATE_DESC_STMT = 'UPDATE roles SET descripcion = %s WHERE id_rol = %s'
    DELETE_ROL_STMT = 'DELETE FROM roles WHERE id_rol = %s'

    def insert_rol(self, nombre, descripcion):
        try:
            super().execute_sql_stmt(self.INSERT_ROL_STMT, (nombre, descripcion))
        except Exception as e:
            raise e
        
    def consult_rol(self, id_rol):
        try:
            rol = super().execute_sql_stmt(self.CONSULT_ROL_STMT, [id_rol], True)
            if len(rol) == 0:
                return None
            return rol[0][0]
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