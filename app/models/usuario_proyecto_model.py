from sys import path as path
path.append('./')
from app.models.connection_model import DbConnectionModel

class UsuarioProyectoModel(DbConnectionModel):
    INSERT_USR_PROY_STMT = 'INSERT INTO usuario_proyecto(username, id_proyecto, fecha_incorporacion, fecha_salida) VALUES (%s, %s, %s, %s)'
    UPDATE_FEC_INC_STMT = 'UPDATE usuario_proyecto SET fecha_incorporacion = %s WHERE username = %s and id_proyecto = %s'
    UPDATE_FEC_SAL_STMT = 'UPDATE usuario_proyecto SET fecha_salida = %s WHERE username = %s and id_proyecto = %s'
    CONSULT_FEC_INC_STMT = 'SELECT fecha_incorporacion FROM usuario_proyecto WHERE username = %s and id_proyecto = %s'
    CONSULT_FEC_SAL_STMT = 'SELECT fecha_salida FROM usuario_proyecto WHERE username = %s and id_proyecto = %s'
    
    def insert_usuario_proyecto(self, username, id_proyecto, fecha_incorporacion, fecha_salida):
        try:
            super().execute_sql_stmt(self.INSERT_USR_PROY_STMT, (username, id_proyecto, fecha_incorporacion, fecha_salida))
        except Exception as e:
            raise e
    
    def update_fecha_incorporacion(self, fecha_incorporacion, username, id_proyecto):
        try:
            super().execute_sql_stmt(self.UPDATE_FEC_INC_STMT, (fecha_incorporacion, username, id_proyecto))
        except Exception as e:
            raise e
    
    def update_fecha_salida(self, fecha_salida, username, id_proyecto):
        try:
            super().execute_sql_stmt(self.UPDATE_FEC_SAL_STMT, (fecha_salida, username, id_proyecto))
        except Exception as e:
            raise e
    
    def consult_fecha_incorporacion(self, username, id_proyecto):
        try:
            fecha_incorporacion = super().execute_sql_stmt(self.CONSULT_FEC_INC_STMT, (username, id_proyecto), True)
            if len(fecha_incorporacion) == 0:
                return None
            return fecha_incorporacion[0][0]
        except Exception as e:
            raise e
    
    def consult_fecha_salida(self, username, id_proyecto):
        try:
            fecha_salida = super().execute_sql_stmt(self.CONSULT_FEC_SAL_STMT, (username, id_proyecto), True)
            if len(fecha_salida) == 0:
                return None
            return fecha_salida[0][0]
        except Exception as e:
            raise e