from sys import path as path
from datetime import datetime
path.append('./')
from app.models.connection_model import DbConnectionModel

class UsuarioProyectoModel(DbConnectionModel):
    INSERT_USR_PROY_STMT = 'INSERT INTO usuario_proyecto(username, id_proyecto, fecha_incorporacion, fecha_salida) VALUES (%s, %s, %s, %s)'
    UPDATE_FEC_SAL_STMT = 'UPDATE usuario_proyecto SET fecha_salida = %s WHERE username = %s AND id_proyecto = %s'
    CONSULT_USUARIOS_STMT = 'SELECT username, fecha_incorporacion, fecha_salida FROM usuario_proyecto WHERE id_proyecto = %s'
    #CONSULT_USUARIOS_DISP_STMT = 'SELECT username FROM usuarios WHERE username NOT IN (SELECT username FROM usuario_proyecto WHERE fecha_salida IS NULL)'

    CONSULT_USUARIOS_DISP_STMT = '''
    SELECT ur.username FROM usuarios_roles ur
    INNER JOIN rol_permiso rp ON rp.id_rol = ur.id_rol
    INNER JOIN permisos p ON p.id_permiso = rp.id_permiso 
    WHERE ur.fin IS NULL AND rp.estado IS TRUE AND
          LOWER(TRIM(both FROM p.nombre)) = 'desarrollo'
          AND username NOT IN 
          (SELECT username FROM usuario_proyecto WHERE fecha_salida IS NULL)'''

    CONSULT_USUARIO_ASIGNADOS_STMT = 'SELECT username FROM usuarios WHERE username IN (SELECT username FROM usuario_proyecto WHERE fecha_salida IS NULL AND id_proyecto = %s)'
    UPDATE_FECHAS_USUARIO_STMT = 'UPDATE usuario_proyecto SET fecha_incorporacion = %s, fecha_salida = %s WHERE username = %s AND id_proyecto = %s'

    CONSULT_USUARIO_ASIGNADOS_FIN_STMT = 'SELECT username FROM usuarios WHERE username IN (SELECT username FROM usuario_proyecto WHERE fecha_salida IS NULL AND id_proyecto = %s )'
    CONSULT_PROY_USUARIO_FIN_STMT = 'SELECT id_proyecto FROM usuario_proyecto WHERE fecha_salida IS NULL AND username = %s'

    def consult_usuarios_asignados_fin(self, id_proyecto):
        try:
            usuarios = super().execute_sql_stmt(self.CONSULT_USUARIO_ASIGNADOS_FIN_STMT, [id_proyecto], True)
            if len(usuarios) == 0:
                return None
            return usuarios
        except Exception as e:
            raise e

    def consult_usuarios_proyecto_fin(self, username):
        try:
            ids_proyectos = super().execute_sql_stmt(self.CONSULT_PROY_USUARIO_FIN_STMT, [username], True)
            if len(ids_proyectos) == 0:
                return None
            return ids_proyectos[0]
        except Exception as e:
            raise e

    def consult_usuarios_asignados(self, id_proyecto):
        try:
            usuarios = super().execute_sql_stmt(self.CONSULT_USUARIO_ASIGNADOS_STMT, [id_proyecto], True)
            if len(usuarios) == 0:
                return None
            return usuarios
        except Exception as e:
            raise e

    def consult_usuarios_disponibles(self):
        try:
            usuarios = super().execute_sql_stmt(self.CONSULT_USUARIOS_DISP_STMT, '', True)
            if len(usuarios) == 0:
                return None
            return usuarios
        except Exception as e:
            raise e

    def consult_usuarios(self, id_proyecto):
        try:
            usuarios = super().execute_sql_stmt(self.CONSULT_USUARIOS_STMT, [id_proyecto], True)
            if len(usuarios) == 0:
                return None
            return usuarios
        except Exception as e:
            raise e
    
    def insert_usuario_proyecto(self, username, id_proyecto):
        try:
            fecha_incorporacion = super().execute_sql_stmt(self.CONSULT_FEC_INC_STMT, (username, id_proyecto), True)
            if len(fecha_incorporacion) == 0:
                super().execute_sql_stmt(self.INSERT_USR_PROY_STMT, (username, id_proyecto, datetime.now(), None))
            else:
                super().execute_sql_stmt(self.UPDATE_FECHAS_USUARIO_STMT, (datetime.now(), None, username, id_proyecto))
        except Exception as e:
            raise e
    
    def update_fecha_salida(self, username, id_proyecto):
        try:
            super().execute_sql_stmt(self.UPDATE_FEC_SAL_STMT, (datetime.now(), username, id_proyecto))
        except Exception as e:
            raise e