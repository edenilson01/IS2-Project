const form = document.getElementById('form-home');
const submitButton = document.getElementById('bt_registrar');

const caja_texto = document.querySelector('input[type=text]');
const checkbox  = document.querySelector('input[type=checkbox]');

caja_texto.addEventListener('keyup', (event) => {
    nombre = caja_texto.value;
    nombre_sin_espacio = String(nombre).trim();
    check_permiso = validar_checkbox();
    if (nombre_sin_espacio == '' && !check_permiso) {
        submitButton.toggleAttribute('disabled', true);
    } else {
        submitButton.toggleAttribute('disabled', false);
    }

})

checkbox.addEventListener('change', (event) => {
    texto_vacio = validar_texto();
    if (!checkbox.checked && texto_vacio) {
        submitButton.toggleAttribute('disabled', true);
    } else {
        submitButton.toggleAttribute('disabled', false);
    }

})

function validar_checkbox() {
    var i = 0;
    var al_menos_uno = false;
    if (checkbox.checked) {
        al_menos_uno = true;                
    }
    return al_menos_uno;
}

function validar_texto() {
    var i = 0;
    var vacio = false;
    nombre = caja_texto.value;
    nombre_sin_espacio = String(nombre).trim();
    if (nombre_sin_espacio == '') {
        vacio= true;                
    }
    return vacio;
}