from sys import path as path
path.append('./')
from app.models.connection_model import DbConnectionModel

class PersonaModel(DbConnectionModel):
    INSERT_PER_STMT = 'INSERT INTO personas(primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, fec_nac) VALUES (%s, %s, %s, %s, %s)'
    UPDATE_PR_NOMBRE_PER_STMT = 'UPDATE personas SET primer_nombre = %s WHERE id_persona = %s'
    UPDATE_SG_NOMBRE_PER_STMT = 'UPDATE personas SET segundo_nombre = %s WHERE id_persona = %s'
    UPDATE_PR_APELLIDO_PER_STMT = 'UPDATE personas SET primer_apellido= %s WHERE id_persona = %s'
    UPDATE_SG_APELLIDO_PER_STMT = 'UPDATE personas SET segundo_apellido = %s WHERE id_persona = %s'
    CONSULT_PER_STMT = 'SELECT * FROM personas WHERE id_persona = %s'
    DELETE_PER_STMT = 'DELETE FROM personas WHERE id_persona = %s'

    def insert_persona(self, pr_nombre, sg_nombre, pr_apellido, sg_apellido, fec_nac):
        try:
            super().execute_sql_stmt(self.INSERT_PER_STMT, (pr_nombre, sg_nombre, pr_apellido, sg_apellido, fec_nac))
        except Exception as e:
            raise e

    def update_pr_nom_persona(self, nombre, id_persona):
        try:
            super().execute_sql_stmt(self.UPDATE_PR_NOMBRE_PER_STMT, (nombre, id_persona))
        except Exception as e:
            raise e
    
    def update_sg_nom_persona(self, nombre, id_persona):
        try:
            super().execute_sql_stmt(self.UPDATE_SG_NOMBRE_PER_STMT, (nombre, id_persona))
        except Exception as e:
            raise e

    def update_pr_ape_persona(self, apellido, id_persona):
        try:
            super().execute_sql_stmt(self.UPDATE_PR_APELLIDO_PER_STMT, (apellido, id_persona))
        except Exception as e:
            raise e
    
    def update_sg_ape_persona(self, apellido, id_persona):
        try:
            super().execute_sql_stmt(self.UPDATE_SG_APELLIDO_PER_STMT, (apellido, id_persona))
        except Exception as e:
            raise e

    def delete_per(self, id_persona):
        try:
            super().execute_sql_stmt(self.DELETE_PER_STMT, [id_persona])
        except Exception as e:
            raise e
    
    def consult_per(self, id_persona):
        try:
            persona = super().execute_sql_stmt(self.CONSULT_PER_STMT, [id_persona], True)
            if len(persona) == 0:
                return None
            return persona[0][0] #VER
        except Exception as e:
            raise e