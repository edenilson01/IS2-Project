--DATOS SEMILLAS
  --Permisos
INSERT INTO permisos(nombre, descripcion) VALUES ('Seguridad', 'Permisos sobre el modulo de seguridad');
INSERT INTO permisos(nombre, descripcion) VALUES ('Proyecto', 'Permisos sobre el modulo de proyecto');
INSERT INTO permisos(nombre, descripcion) VALUES ('Desarrollo', 'Permisos sobre el modulo de desarrollo');

  --Roles
INSERT INTO roles(nombre, descripcion) VALUES ('Super Usuario', 'Tienen accesos a todos los modulos');
INSERT INTO roles(nombre, descripcion) VALUES ('Seguridad', 'Acceso al modulo de seguridad');
INSERT INTO roles(nombre, descripcion) VALUES ('Proyecto', 'Acceso al modulo de proyecto');
INSERT INTO roles(nombre, descripcion) VALUES ('Desarrollo', 'Acceso al modulo de desarrollo');
  
    --Roles, Permisos
INSERT INTO rol_permiso(id_rol, id_permiso, estado) 
VALUES ((SELECT id_rol FROM roles WHERE UPPER(nombre) LIKE 'SUPER USUARIO'), (SELECT id_permiso FROM permisos WHERE UPPER(nombre) LIKE 'PROYECTO'), true);

INSERT INTO rol_permiso(id_rol, id_permiso, estado) 
VALUES ((SELECT id_rol FROM roles WHERE UPPER(nombre) LIKE 'SUPER USUARIO'), (SELECT id_permiso FROM permisos WHERE UPPER(nombre) LIKE 'SEGURIDAD'), true);

INSERT INTO rol_permiso(id_rol, id_permiso, estado) 
VALUES ((SELECT id_rol FROM roles WHERE UPPER(nombre) LIKE 'SUPER USUARIO'), (SELECT id_permiso FROM permisos WHERE UPPER(nombre) LIKE 'DESARROLLO'), true);

INSERT INTO rol_permiso(id_rol, id_permiso, estado) 
VALUES ((SELECT id_rol FROM roles WHERE UPPER(nombre) LIKE 'SEGURIDAD'), (SELECT id_permiso FROM permisos WHERE UPPER(nombre) LIKE 'SEGURIDAD'), true);

INSERT INTO rol_permiso(id_rol, id_permiso, estado) 
VALUES ((SELECT id_rol FROM roles WHERE UPPER(nombre) LIKE 'PROYECTO'), (SELECT id_permiso FROM permisos WHERE UPPER(nombre) LIKE 'PROYECTO'), true);

INSERT INTO rol_permiso(id_rol, id_permiso, estado) 
VALUES ((SELECT id_rol FROM roles WHERE UPPER(nombre) LIKE 'DESARROLLO'), (SELECT id_permiso FROM permisos WHERE UPPER(nombre) LIKE 'DESARROLLO'), true);

  --Usuario
    --Personas
INSERT INTO personas(primer_nombre, primer_apellido, fec_nac)
VALUES ('Richard', 'Cabrera', '14-02-1998');

INSERT INTO personas(primer_nombre, primer_apellido, fec_nac)
VALUES ('Edenilson', 'Dominguez', '31-12-1998');

INSERT INTO personas(primer_nombre, primer_apellido, fec_nac)
VALUES ('Johana', 'Pineda', '15-06-1998');

INSERT INTO personas(primer_nombre, primer_apellido, fec_nac)
VALUES ('Alejandra', 'Vega', '27-09-1998');

    --Usuarios
INSERT INTO usuarios(username, password, id_persona, correo, estado)
VALUES ('rich', '1234', (SELECT id_persona FROM personas WHERE UPPER(primer_nombre) LIKE 'RICHARD'), 'rich@correo.com', true);

INSERT INTO usuarios(username, password, id_persona, correo, estado)
VALUES ('ede', 'abcd0123', (SELECT id_persona FROM personas WHERE UPPER(primer_nombre) LIKE 'EDENILSON'), 'ede@correo.com', true);

INSERT INTO usuarios(username, password, id_persona, correo, estado)
VALUES ('joha', 'unicornio', (SELECT id_persona FROM personas WHERE UPPER(primer_nombre) LIKE 'JOHANA'), 'joha@correo.com', true);

INSERT INTO usuarios(username, password, id_persona, correo, estado)
VALUES ('ale', 'avril', (SELECT id_persona FROM personas WHERE UPPER(primer_nombre) LIKE 'ALEJANDRA'), 'ale@correo.com', true);

  --Usuario, Roles
INSERT INTO usuarios_roles(id_rol, username, inicio)
VALUES ((SELECT id_rol FROM roles WHERE UPPER(nombre) LIKE 'SUPER USUARIO'), 'ede', now());

INSERT INTO usuarios_roles(id_rol, username, inicio)
VALUES ((SELECT id_rol FROM roles WHERE UPPER(nombre) LIKE 'SEGURIDAD'), 'joha', now());

INSERT INTO usuarios_roles(id_rol, username, inicio)
VALUES ((SELECT id_rol FROM roles WHERE UPPER(nombre) LIKE 'PROYECTO'), 'ale', now());

INSERT INTO usuarios_roles(id_rol, username, inicio)
VALUES ((SELECT id_rol FROM roles WHERE UPPER(nombre) LIKE 'DESARROLLO'), 'rich', now());