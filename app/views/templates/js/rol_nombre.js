const form = document.getElementById('form-crear_rol');
const submitButton = document.getElementById('asig_perm');

document.querySelectorAll('.form-box').forEach((box) => {
    const boxInput = box.querySelector('input');

    boxInput.addEventListener('keyup', (event) => {
        check_name = false;
        nombre = boxInput.value;
        nombre_sin_espacio = String(nombre).trim();
        if (nombre_sin_espacio == '') {
            submitButton.toggleAttribute('disabled', true);
        } else {
            submitButton.toggleAttribute('disabled', false);
        }
    });
});

