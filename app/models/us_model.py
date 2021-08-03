from _typeshed import Self
from sys import path as path
path.append('./')
from app.models.connection_model import DbConnectionModel

class USModel(DbConnectionModel):
    INSERT_US_STMT = 'INSERT INTO us(nombre, descripcion, estado, username, id_proyecto, id_sprint, backlog) VALUES (%s, %s, %s, %s, %s, %s, %s)'
    UPDATE_NOM_US_STMT = 'UPDATE us SET nombre = %s WHERE id_us = %s'
    UPDATE_DESC_US_STMT = 'UPDATE us SET descripcion = %s WHERE id_us = %s'
    UPDATE_EST_US_STMT = 'UPDATE us SET estado = %s WHERE id_us = %s'
    UPDATE_USERNAME_US_STMT = 'UPDATE us SET username = %s WHERE id_us = %s'
    UPDATE_SPRINT_US_STMT = 'UPDATE us SET id_sprint = %s WHERE id_us = %s'
    UPDATE_BACKLOG_STMT = 'UPDATE us SET backlog = %s WHERE id_us = %s'
    CONSULT_ESTADO_STMT = 'SELECT backlog FROM us WHERE id_us = %s'

    def insert_us(self, nombre, descripcion, estado, username, id_proyecto, id_sprint, backlog):
        try:
            super().execute_sql_stmt(self.INSERT_US_STMT, (nombre, descripcion, estado, username, id_proyecto, id_sprint, backlog))
        except Exception as e:
            raise e
    
    def update_nombre(self, nombre, id_us):
        try: 
            super().execute_sql_stmt(self.UPDATE_NOM_US_STMT, (nombre, id_us))
        except Exception as e:
            raise e
    
    def update_descripcion(self, descripcion, id_us):
        try:
            super().execute_sql_stmt(self.UPDATE_DESC_US_STMT, (descripcion, id_us))
        except Exception as e:
            raise e
    
    def update_estado(self, estado, id_us):
        try:
            super().execute_sql_stmt(self.UPDATE_EST_US_STMT, (estado, id_us))
        except Exception as e:
            raise e
    
    def update_username(self, username, id_us):
        try:
            super().execute_sql_stmt(self.UPDATE_USERNAME_US_STMT, (username, id_us))
        except Exception as e:
            raise e
    
    def update_sprint_us(self, sprint, id_us):
        try:
            super().execute_sql_stmt(self.UPDATE_SPRINT_US_STMT, (sprint, id_us))
        except Exception as e:
            raise e

    def update_backlog_state(self, state, id_us):
        try:
            super().execute_sql_stmt(self.UPDATE_BACKLOG_STMT, (state, id_us))
        except Exception as e:
            raise e
    
    def consult_state(self, id_us):
        try:
            state = super().execute_sql_stmt(self.CONSULT_ESTADO_STMT, [id_us], True)
            if len(state) == 0:
                return None
            return state[0][0]
        except Exception as e:
            raise e