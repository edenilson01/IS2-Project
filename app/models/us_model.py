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
    UPDATE_BACKLOG_STMT = 'UPDATE us SET backlog = %s WHERE id_us = %s '
    UPDATE_SPRINT_STMT = 'UPDATE us SET id_sprint = %s WHERE id_sprint = %s '
    UPDATE_US_STMT = 'UPDATE us SET nombre = %s, descripcion = %s, username =%s WHERE id_us = %s'
    CONSULT_ESTADO_BACKLOG_STMT = 'SELECT backlog FROM us WHERE backlog = false AND id_sprint = %s'
    CONSULT_US_BY_ID_STMT = 'SELECT nombre, descripcion FROM us WHERE username = %s'  
    CONSULT_US_BY_SPRINT_STMT = 'SELECT id_us, nombre, descripcion, estado, username FROM us WHERE backlog = false AND id_sprint = %s' 
    CONSULT_USERNAME_STMT = 'SELECT username from us'
    CONSULT_US_BY_PROYECT_BACKLOG_STMT = 'SELECT *  FROM us WHERE id_proyecto = %s AND backlog IS True'  
    #CONSULT_US_BY_PROYECT_KANBAN_STMT = 'SELECT *  FROM us WHERE id_proyecto = %s AND backlog IS False'  
    CONSULT_US_BY_PROYECT_KANBAN_STMT = "SELECT us.*, p.primer_nombre || ' ' || p.primer_apellido FROM us us inner join usuarios u ON u.username = us.username inner join personas p on p.id_persona = u.id_persona WHERE id_proyecto = %s AND backlog IS False AND us.id_sprint = (SELECT sp.id_sprint FROM sprints sp WHERE activo IS TRUE AND sp.id_proyecto = %s)"
    CONSULT_US_BY_ID_STMT = 'SELECT nombre, descripcion FROM us WHERE username = %s'
    CONSULT_US_BY_ID_SPRINT_STMT = 'SELECT estado FROM us WHERE id_sprint = %s AND estado <> \'DONE\''
    CONSULT_USERNAME_STMT = 'SELECT username from us'    
    CONSULT_US_STMT = 'SELECT id_us, nombre, descripcion, username FROM US WHERE id_proyecto = %s'
    CONSULT_NOM_US_SMTM ='SELECT nombre FROM us WHERE id_us = %s'
    CONSULT_DESC_US_SMTM ='SELECT descripcion FROM us WHERE id_us = %s'
    DELETE_US_STMT = 'DELETE FROM US WHERE id_us = %s'
    UPDATE_USERNAME_STMT = 'UPDATE us SET username = %s WHERE id_us = %s'
    
    def consult_backlog_by_id_sprint(self, id_sprint):
        try:
            us = super().execute_sql_stmt(self.CONSULT_ESTADO_BACKLOG_STMT, [id_sprint], True)
            if len(us) == 0:
                return None
            return us
        except Exception as e:
            raise e    

    def consult_us_by_id_sprint(self, id_sprint):
        try:
            us = super().execute_sql_stmt(self.CONSULT_US_BY_ID_SPRINT_STMT, [id_sprint], True)
            if len(us) == 0:
                return None
            return us
        except Exception as e:
            raise e    
    
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

    def consult_us_by_proyect_kanban(self, id_project):
        try:
            us = super().execute_sql_stmt(self.CONSULT_US_BY_PROYECT_KANBAN_STMT, (id_project, id_project), True)
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
    
    def update_sprint(self, id_sprint):
        try:
            super().execute_sql_stmt(self.UPDATE_SPRINT_STMT, (id_sprint))
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

    def consult_username(self):
        try:
            username = super().execute_sql_stmt(self.CONSULT_USERNAME_STMT, '', True)
            if len(username) == 0:
                return None
            return username
        except Exception as e:
            raise e

    def consult_nombre_us(self, id_us):
        try:
            nombre = super().execute_sql_stmt(self.CONSULT_NOM_US_SMTM,  [id_us], True)
            if len(nombre) == 0:
                return None
            return nombre [0][0]
        except Exception as e:
            raise e

    def consult_descripcion_us(self, id_us):
        try:
            descripcion= super().execute_sql_stmt(self.CONSULT_DESC_US_SMTM, [id_us], True)
            if len(descripcion) == 0:
                return None
            return descripcion [0][0]
        except Exception as e:
            raise e


    def delete_us(self, id_us):
        try:
            super().execute_sql_stmt(self.DELETE_US_STMT, [id_us])
        except Exception as e:
            raise e

    def update_username(self, username, id_us):
        try:
            super().execute_sql_stmt(self.UPDATE_USERNAME_STMT, (username, id_us))
        except Exception as e:
            raise e
       