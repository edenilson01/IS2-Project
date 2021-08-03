from sys import path as path
path.append('./')
from app.models.connection_model import DbConnectionModel

class ProyectoModel(DbConnectionModel):
    INSERT_PROJECT_STMT = 'INSERT INTO proyectos(nombre, estado, fecha_inicio, fecha_fin) VALUES (%s, %s, %s, %s)'
    UPDATE_NOMBRE_STMT = 'UPDATE proyectos SET nombre = %s WHERE id_proyecto = %s'
    UPDATE_ESTADO_STMT = 'UPDATE proyectos SET estado = %s WHERE id_proyecto = %s'
    UPDATE_FECHA_INI_STMT = 'UPDATE proyectos SET fecha_inicio = %s WHERE id_proyecto = %s'
    UPDATE_FECHA_FIN_STMT = 'UPDATE proyectos SET fecha_fin = %s WHERE id_proyecto = %s'
    CONSULT_ESTADO_STMT = 'SELECT estado FROM proyectos WHERE id_proyecto = %s'

    def insert_project(self, nombre, estado, fecha_inicio, fecha_fin):
        try:
            super().execute_sql_stmt(self.INSERT_PROJECT_STMT, (nombre, estado, fecha_inicio, fecha_fin))
        except Exception as e:
            raise e
    
    def update_nombre(self, nombre, id_proyecto):
        try:
            super().execute_sql_stmt(self.UPDATE_NOMBRE_STMT, (nombre, id_proyecto))
        except Exception as e:
            raise e
    
    def update_estado(self, estado, id_proyecto):
        try:
            super().execute_sql_stmt(self.UPDATE_ESTADO_STMT, (estado, id_proyecto))
        except Exception as e:
            raise e
    
    def update_fecha_inicio(self, fecha_inicio, id_proyecto):
        try:
            super().execute_sql_stmt(self.UPDATE_FECHA_INI_STMT, (fecha_inicio, id_proyecto))
        except Exception as e:
            raise e
    
    def update_fecha_fin(self, fecha_fin, id_proyecto):
        try:
            super().execute_sql_stmt(self.UPDATE_FECHA_FIN_STMT, (fecha_fin, id_proyecto))
        except Exception as e:
            raise e

    def consult_estado(self, id_proyecto):
        try:
            estado = super().execute_sql_stmt(self.CONSULT_ESTADO_STMT, [id_proyecto], True)
            if len(estado) == 0:
                return None
            return estado[0][0]
        except Exception as e:
            raise e