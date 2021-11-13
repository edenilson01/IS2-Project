from contextlib import ExitStack
from sys import path as path
from datetime import datetime
path.append('./')
from app.models.connection_model import DbConnectionModel

class SprintModel(DbConnectionModel):
    INSERT_SPRINT_STMT = 'INSERT INTO sprints(nombre, inicio, fin, activo, id_proyecto) VALUES (%s, %s, %s, %s, %s)'
    INSERT_STMT = "INSERT INTO sprints(nombre, id_proyecto) VALUES (%s, %s)"
    UPDATE_FECHA_INI_STMT = 'UPDATE sprints SET inicio = %s WHERE id_sprint = %s'
    UPDATE_FECHA_FIN_STMT = 'UPDATE sprints SET fin = %s WHERE id_sprint = %s'
    UPDATE_ESTADO_STMT = 'UPDATE sprints SET activo = %s WHERE id_sprint = %s'
    UPDATE_NOMBRE_STMT = 'UPDATE sprints SET nombre = %s WHERE id_sprint = %s'
    CONSULT_US_STMT = 'SELECT id_sprint, nombre, inicio, fin, activo FROM sprints WHERE id_proyecto = %s'
    CONSULT_ESTADO_SPRINTS_STMT = 'SELECT id_sprint FROM sprints WHERE id_proyecto = %s AND fin IS NOT NULL AND activo IS FALSE'
    CONSULT_SPRINT_STMT = 'SELECT nombre FROM sprints WHERE id_sprint = %s'
    CONSULT_SPRINT_ACTIVO_STMT = 'SELECT nombre FROM sprints WHERE id_proyecto = %s AND ACTIVO IS TRUE'
    UPDATE_SPRINT_STMT = 'UPDATE sprints SET nombre = %s, inicio = %s, fin = %s, activo = %s WHERE id_sprint = %s'
    CONSULTAR_SPRINT_ACTIVO = 'select s.activo from sprints s where s.activo is true and s.id_proyecto = %s;'

    def sprint_activo(self, id):
        try:
            res = super().execute_sql_stmt(self.CONSULTAR_SPRINT_ACTIVO, [id], True)
            if not res:
                return False
            else:
                return res[0][0]
        except Exception as e:
            raise e

    def consult_sprint_activo(self, id_proyect):
        try:
            sprint = super().execute_sql_stmt(self.CONSULT_SPRINT_ACTIVO_STMT, [id_proyect], True)
            if len(sprint) == 0:
                return None
            return sprint [0][0]
        except Exception as e:
            raise e

    def consult_estados(self, id_proyecto):
        try:
            estados = super().execute_sql_stmt(self.CONSULT_ESTADO_SPRINTS_STMT, [id_proyecto], True)
            if len(estados) == 0:
                return None
            return estados
        except Exception as e:
            raise e


    def consult_sprint(self, id):
        try:
            sp = super().execute_sql_stmt(self.CONSULT_SPRINT_STMT, [id], True)
            if len(sp) == 0:
                return None
            return sp[0]
        except Exception as e:
            raise e


    def consult(self, id):
        try:
            sp = super().execute_sql_stmt(self.CONSULT_US_STMT, [id], True)
            if len(sp) == 0:
                return None
            return sp
        except Exception as e:
            raise e

    def insert_sprint_short(self, nombre, id_proyecto):
        try:
            super().execute_sql_stmt(self.INSERT_STMT, (nombre, id_proyecto))
        except Exception as e:
            raise e

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
    
    def update_fecha_fin(self, id_sprint):
        try:
            super().execute_sql_stmt(self.UPDATE_FECHA_FIN_STMT, (datetime.now(), id_sprint))
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

    def update_sprint(self, nombre, fecha_inicio, fecha_fin, id_sprint):
        try:
            super().execute_sql_stmt(self.UPDATE_SPRINT_STMT, (nombre, fecha_inicio, fecha_fin, True, id_sprint))
        except Exception as e:
            raise e            