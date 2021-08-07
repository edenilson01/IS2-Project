from sys import path as path
path.append('./')
from app.models.connection_model import DbConnectionModel

class RolPermisoModel(DbConnectionModel):
    INSERT_ROL_PER_STMT = 'INSERT INTO rol_permiso(id_rol, id_permiso, estado) VALUES (%s, %s, %s)'
    UPDATE_ROL_PER_STMT = 'UPDATE rol_permiso SET estado = %s WHERE id_rol = %s and id_permiso = %s'
    DELETE_ROL_PER_STMT = 'DELETE FROM rol_permiso WHERE id_rol = %s and id_permiso = %s'
    CONSULT_ROL_PER_STMT = 'SELECT estado FROM rol_permiso WHERE id_rol = %s and id_permiso = %s'

    def insert_rol_permiso(self, id_rol, id_permiso, estado):
        try:
            super().execute_sql_stmt(self.INSERT_ROL_PER_STMT, (id_rol, id_permiso, estado))
        except Exception as e:
            raise e

    def update_rol_permiso(self, estado, id_rol, id_permiso):
        try:
            super().execute_sql_stmt(self.UPDATE_ROL_PER_STMT, (estado, id_rol, id_permiso))
        except Exception as e:
            raise e
    
    def delete_rol_permiso(self, id_rol, id_permiso):
        try:
            super().execute_sql_stmt(self.DELETE_ROL_PER_STMT, (id_rol, id_permiso))
        except Exception as e:
            raise e
    
    def consult_estado(self, id_rol, id_permiso):
        try:
            estado = super().execute_sql_stmt(self.CONSULT_ROL_PER_STMT, (id_rol, id_permiso), True)
            if len(estado) == 0:
                return None
            return estado[0][0]
        except Exception as e:
            raise e
                