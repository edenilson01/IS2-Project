from contextlib import ExitStack
from sys import path as path
path.append('./')
from app.models.connection_model import DbConnectionModel

class SprintModel(DbConnectionModel):
    INSERT_SPRINT_STMT = 'INSERT INTO sprints(nombre, inicio, fin, activo, id_proyecto) VALUES (%s, %s, %s, %s, %s)'
    UPDATE_FECHA_INI_STMT = 'UPDATE sprints SET inicio = %s WHERE id_sprint = %s'
    UPDATE_FECHA_FIN_STMT = 'UPDATE sprints SET fin = %s WHERE id_sprints = %s'
    UPDATE_ESTADO_STMT = 'UPDATE sprints SET activo = %s WHERE id_sprints = %s'
    UPDATE_NOMBRE_STMT = 'UPDATE sprints SET nombre = %s WHERE id_sprints = %s'

    def insert_sprint(self, nombre, fec_inicio, fec_fin, estado, id_proyecto):
        try:
            super().execute_sql_stmt(self.INSERT_SPRINT_STMT, (nombre, fec_inicio, fec_fin, estado, id_proyecto))
        except Exception as e:
            raise e
    
    def update_fecha_inicio(self, fecha_inicio, id_sprint):
        try:
            super().execute_sql_stmt(self.UPDATE_FECHA_INI_STMT, (fecha_inicio, id_sprint))
        except Exception as e:
            raise e
    
    def update_fecha_fin(self, fecha_fin, id_sprint):
        try:
            super().execute_sql_stmt(self.UPDATE_FECHA_FIN_STMT, (fecha_fin, id_sprint))
        except Exception as e:
            raise e
    
    def update_estado(self, estado, id_sprint):
        try:
            super().execute_sql_stmt(self.UPDATE_ESTADO_STMT, (estado, id_sprint))
        except Exception as e:
            raise e
    
    def update_nombre(self, nombre, id_sprint):
        try:
            super().execute_sql_stmt(self.UPDATE_NOMBRE_STMT, (nombre, id_sprint))
        except Exception as e:
            raise e