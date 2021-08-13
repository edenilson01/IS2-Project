const form = document.getElementById('form-crear_rol');
const submitButton = document.getElementById('guardar');

function habilitar() {
    lista_perm  = document.querySelectorAll('.permisos');
    var i = 0;
    var al_menos_uno = false;
    //Recorrido de checkbox's
    while (i < lista_perm.length) {
        // Verifica si el elemento es un checkbox
        if (lista_perm[i].tagName == 'INPUT' && lista_perm[i].type == 'checkbox') {
            lista_perm[i].toggleAttribute('disabled', false);
        }
        i++
        
    }
}

document.querySelectorAll('.permisos').forEach((box) => {

    addEventListener('change', (event) => {
        
        check_permiso = validar_checkbox();
        if (!check_permiso) {
            submitButton.toggleAttribute('disabled', true);
        } else {
            submitButton.toggleAttribute('disabled', false);
        }
    });
});

function validar_checkbox() {
    checkboxes  = document.querySelectorAll('.permisos');
    var i = 0;
    var al_menos_uno = false;
    //Recorrido de checkbox's
    while (i < checkboxes.length) {
        // Verifica si el elemento es un checkbox
        if (checkboxes[i].tagName == 'INPUT' && checkboxes[i].type == 'checkbox') {
            // Verifica si esta checked
            if (checkboxes[i].checked) {
                al_menos_uno = true;             
                return al_menos_uno;
            }
        }
        i++
        
    }
}