const form = document.getElementById('form-home');
const submitButton = document.getElementById('bt_registrar');
const caja_texto1 = document.querySelector('input[type=text]');


caja_texto1.addEventListener('keyup', (event) => {
    nombre = caja_texto1.value;
    nombre_sin_espacio = String(nombre).trim();
    descripcion = caja_texto1.value;
    descripcion_sin_espacio = String(descripcion).trim();
       
    if (nombre_sin_espacio == '' && !descripcion_sin_espacio) {
        submitButton.toggleAttribute('disabled', true);
    } else {
        submitButton.toggleAttribute('disabled', false);
    }

})






