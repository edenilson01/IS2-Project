#from _typeshed import Self
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
    UPDATE_US_STMT = 'UPDATE us SET nombre = %s, descripcion = %s, username =%s WHERE id_us = %s'    
    CONSULT_ESTADO_STMT = 'SELECT backlog FROM us WHERE id_us = %s'
    CONSULT_US_BY_ID_STMT = 'SELECT nombre, descripcion FROM us WHERE username = %s'  
    CONSULT_US_BY_SPRINT_STMT = 'SELECT id_us, nombre, descripcion FROM us WHERE id_sprint = %s' 
    CONSULT_US_BY_ID_2_STMT = 'SELECT nombre, descripcion, estado, user_name, id_proyecto FROM us WHERE id_us = %s'    
    CONSULT_USERNAME_STMT = 'SELECT username from us'  
    CONSULT_US_BY_PROYECT_BACKLOG_STMT = 'SELECT *  FROM us WHERE id_proyecto = %s AND backlog IS True'  
    CONSULT_US_STMT = 'SELECT id_us, nombre, descripcion, username FROM US WHERE id_proyecto = %s'
    DELETE_US_STMT = 'DELETE FROM US WHERE id_us = %s'

    def consult_us_by_id(self, id_us):
        try:
            us = super().execute_sql_stmt(self.CONSULT_US_BY_ID_STMT, [id_us], True)
            if len(us) == 0:
                return None
            return us[0]
        except Exception as e:
            raise e    
      
    def consult_us_by_proyect_backlog(self, id_project):
        try:
            us = super().execute_sql_stmt(self.CONSULT_US_BY_PROYECT_BACKLOG_STMT, [id_project], True)
            if len(us) == 0:
                return None
            return us
        except Exception as e:
            raise e

    def consult_us_by_sprint(self, id_sprint):
        try:
            us = super().execute_sql_stmt(self.CONSULT_US_BY_SPRINT_STMT, [id_sprint], True)
            if len(us) == 0:
                return None
            return us
        except Exception as e:
            raise e

    def insert_us(self, nombre, descripcion, estado, username, id_proyecto, id_sprint, backlog):
        try:
            super().execute_sql_stmt(self.INSERT_US_STMT, (nombre, descripcion, estado, username, id_proyecto, id_sprint, backlog))
        except Exception as e:
            raise e

    def update_us(self, nombre, decripcion, username, id_us):
        try:
            super().execute_sql_stmt(self.UPDATE_US_STMT, (nombre, decripcion, username, id_us))
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

    def consult_us(self, id):
        try:
            us = super().execute_sql_stmt(self.CONSULT_US_STMT, [id], True)
            if len(us) == 0:
                return None
            return us
        except Exception as e:
            raise e
    
    def consult_us_by_id_2(self, id):
        try:
            us = super().execute_sql_stmt(self.CONSULT_US_BY_ID_2_STMT, [id], True)
            if len(us) == 0:
                return None
            return us
        except Exception as e:
            raise e
    

    def consult_username(self):
        try:
            username = super().execute_sql_stmt(self.CONSULT_USERNAME_STMT, '', True)
            if len(username) == 0:
                return None
            return username
        except Exception as e:
            raise e

    def delete_us(self, id_us):
        try:
            super().execute_sql_stmt(self.DELETE_US_STMT, [id_us])
        except Exception as e:
            raise e