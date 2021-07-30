CREATE DATABASE is2_project --nombre de la base de datos

CREATE SEQUENCE public.proyectos_id_proyecto_seq;

CREATE TABLE public.PROYECTOS (
                id_proyecto BIGINT NOT NULL DEFAULT nextval('public.proyectos_id_proyecto_seq'),
                nombre VARCHAR NOT NULL,
                estado BOOLEAN NOT NULL,
                CONSTRAINT proyectos_pk PRIMARY KEY (id_proyecto)
);


ALTER SEQUENCE public.proyectos_id_proyecto_seq OWNED BY public.PROYECTOS.id_proyecto;

CREATE SEQUENCE public.backlog_id_backlog_seq;

CREATE TABLE public.BACKLOG (
                id_backlog NUMERIC NOT NULL DEFAULT nextval('public.backlog_id_backlog_seq'),
                id_proyecto BIGINT NOT NULL,
                CONSTRAINT backlog_pk PRIMARY KEY (id_backlog)
);


ALTER SEQUENCE public.backlog_id_backlog_seq OWNED BY public.BACKLOG.id_backlog;

CREATE TABLE public.SPRINTS (
                id_sprint NUMERIC NOT NULL,
                nombre VARCHAR(30) NOT NULL,
                inicio DATE,
                fin DATE,
                activo BOOLEAN DEFAULT FALSE NOT NULL,
                id_proyecto BIGINT NOT NULL,
                CONSTRAINT sprints_pk PRIMARY KEY (id_sprint)
);


CREATE SEQUENCE public.permisos_id_permiso_seq;

CREATE TABLE public.PERMISOS (
                id_permiso BIGINT NOT NULL DEFAULT nextval('public.permisos_id_permiso_seq'),
                nombre VARCHAR(30) NOT NULL,
                descripcion VARCHAR(50),
                CONSTRAINT permisos_pk PRIMARY KEY (id_permiso)
);


ALTER SEQUENCE public.permisos_id_permiso_seq OWNED BY public.PERMISOS.id_permiso;

CREATE SEQUENCE public.roles_id_rol_seq;

CREATE TABLE public.ROLES (
                id_rol BIGINT NOT NULL DEFAULT nextval('public.roles_id_rol_seq'),
                nombre VARCHAR(30) NOT NULL,
                descripcion VARCHAR(50),
                CONSTRAINT roles_pk PRIMARY KEY (id_rol)
);


ALTER SEQUENCE public.roles_id_rol_seq OWNED BY public.ROLES.id_rol;

CREATE TABLE public.ROL_PERMISO (
                id_rol BIGINT NOT NULL,
                id_permiso BIGINT NOT NULL,
                estado BOOLEAN NOT NULL,
                CONSTRAINT rol_permiso_pk PRIMARY KEY (id_rol, id_permiso)
);


CREATE TABLE public.PERSONAS (
                id_persona NUMERIC NOT NULL,
                primer_nombre VARCHAR(50) NOT NULL,
                segundo_nombre VARCHAR(50),
                primer_apellido VARCHAR(50) NOT NULL,
                segundo_apellido VARCHAR(50),
                fec_nac DATE NOT NULL,
                CONSTRAINT personas_pk PRIMARY KEY (id_persona)
);


CREATE TABLE public.USUARIOS (
                username VARCHAR(15) NOT NULL,
                password VARCHAR(15) NOT NULL,
                id_persona NUMERIC NOT NULL,
                correo VARCHAR(100) NOT NULL,
                CONSTRAINT usuarios_pk PRIMARY KEY (username)
);


CREATE TABLE public.USUARIOS_ROLES (
                id_rol BIGINT NOT NULL,
                username VARCHAR(15) NOT NULL,
                inicio DATE NOT NULL,
                fin DATE,
                CONSTRAINT usuarios_roles_pk PRIMARY KEY (id_rol, username)
);


CREATE SEQUENCE public.us_id_us_seq;

CREATE SEQUENCE public.sprints_id_sprint_seq;

CREATE TABLE public.US (
                id_us BIGINT NOT NULL DEFAULT nextval('public.us_id_us_seq'),
                nombre VARCHAR(30) NOT NULL,
                descripcion VARCHAR,
                estado VARCHAR NOT NULL,
                id_backlog NUMERIC,
                id_sprint NUMERIC DEFAULT nextval('public.sprints_id_sprint_seq'),
                username VARCHAR(15),
                CONSTRAINT us_pk PRIMARY KEY (id_us)
);


ALTER SEQUENCE public.us_id_us_seq OWNED BY public.US.id_us;

ALTER SEQUENCE public.sprints_id_sprint_seq OWNED BY public.US.id_sprint;

CREATE SEQUENCE public.usuario_proyecto_id_usuario_proyecto_seq;

CREATE TABLE public.USUARIO_PROYECTO (
                id_usuario_proyecto BIGINT NOT NULL DEFAULT nextval('public.usuario_proyecto_id_usuario_proyecto_seq'),
                username VARCHAR(15) NOT NULL,
                id_proyecto BIGINT NOT NULL,
                CONSTRAINT usuario_proyecto_pk PRIMARY KEY (id_usuario_proyecto)
);


ALTER SEQUENCE public.usuario_proyecto_id_usuario_proyecto_seq OWNED BY public.USUARIO_PROYECTO.id_usuario_proyecto;

ALTER TABLE public.USUARIO_PROYECTO ADD CONSTRAINT proyectos_usuario_proyecto_fk
FOREIGN KEY (id_proyecto)
REFERENCES public.PROYECTOS (id_proyecto)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.SPRINTS ADD CONSTRAINT proyectos_sprints_fk
FOREIGN KEY (id_proyecto)
REFERENCES public.PROYECTOS (id_proyecto)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.BACKLOG ADD CONSTRAINT proyectos_backlog_fk
FOREIGN KEY (id_proyecto)
REFERENCES public.PROYECTOS (id_proyecto)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.US ADD CONSTRAINT backlog_us_fk
FOREIGN KEY (id_backlog)
REFERENCES public.BACKLOG (id_backlog)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.US ADD CONSTRAINT sprints_us_fk
FOREIGN KEY (id_sprint)
REFERENCES public.SPRINTS (id_sprint)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.ROL_PERMISO ADD CONSTRAINT permisos_rol_permiso_fk
FOREIGN KEY (id_permiso)
REFERENCES public.PERMISOS (id_permiso)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.ROL_PERMISO ADD CONSTRAINT roles_rol_permiso_fk
FOREIGN KEY (id_rol)
REFERENCES public.ROLES (id_rol)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.USUARIOS_ROLES ADD CONSTRAINT roles_usuarios_roles_fk
FOREIGN KEY (id_rol)
REFERENCES public.ROLES (id_rol)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.USUARIOS ADD CONSTRAINT personas_usuarios_fk
FOREIGN KEY (id_persona)
REFERENCES public.PERSONAS (id_persona)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.USUARIO_PROYECTO ADD CONSTRAINT usuarios_usuario_proyecto_fk
FOREIGN KEY (username)
REFERENCES public.USUARIOS (username)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.US ADD CONSTRAINT usuarios_us_fk
FOREIGN KEY (username)
REFERENCES public.USUARIOS (username)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.USUARIOS_ROLES ADD CONSTRAINT usuarios_usuarios_roles_fk
FOREIGN KEY (username)
REFERENCES public.USUARIOS (username)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;