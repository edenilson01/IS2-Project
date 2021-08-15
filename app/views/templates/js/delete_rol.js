const submitButton = document.getElementById('eliminar');

function habilitar(selected) {
    if (selected == 0) {
        submitButton.toggleAttribute('disabled', true);
    } else {
        submitButton.toggleAttribute('disabled', false);
    }
}
