from sys import path as path
path.append('./')
from app.models.connection_model import DbConnectionModel

class RolPermisoModel(DbConnectionModel):
    INSERT_ROL_PER_STMT = 'INSERT INTO rol_permiso(id_rol, id_permiso, estado) VALUES (%s, %s, %s)'
    UPDATE_ROL_PER_STMT = 'UPDATE rol_permiso SET estado = %s WHERE id_rol = %s and id_permiso = %s'
    CONSULT_ROL_PER_STMT = 'SELECT estado FROM rol_permiso WHERE id_rol = %s and id_permiso = %s'
    CONSULT_PERS_STMT_2 = 'SELECT id_permiso FROM rol_permiso WHERE id_rol = %s and estado = True'
    CONSULT_ROLES_PERMISO_STMT = 'SELECT id_rol FROM rol_permiso WHERE id_permiso = %s'
    CONSULT_PERS_STMT = 'SELECT per.nombre FROM rol_permiso rp JOIN permisos per ON per.id_permiso = rp.id_permiso WHERE rp.id_rol = %s'

    def consult_roles_permiso(self, id_permiso):
        try:
            roles = super().execute_sql_stmt(self.CONSULT_ROLES_PERMISO_STMT, [id_permiso], True)
            if len(roles) == 0:
                return None
            return roles[0]
        except Exception as e:
            raise e
    
    def consult_permisos(self, id_rol):
        try:
            permisos = super().execute_sql_stmt(self.CONSULT_PERS_STMT, [id_rol], True)
           
            if len(permisos) == 0:
                return None
            return permisos
        except Exception as e:
            raise e

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
    
    def consult_estado(self, id_rol, id_permiso):
        try:
            estado = super().execute_sql_stmt(self.CONSULT_ROL_PER_STMT, (id_rol, id_permiso), True)
            if len(estado) == 0:
                return None
            return estado[0][0]
        except Exception as e:
            raise e
    
    def consult_permisos2(self, id_rol):
        try:
            permisos = super().execute_sql_stmt(self.CONSULT_PERS_STMT_2, [id_rol], True)
           
            if len(permisos) == 0:
                return None
            return permisos
        except Exception as e:
            raise e