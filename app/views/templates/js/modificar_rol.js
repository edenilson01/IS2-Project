
const submitButton = document.getElementById('guardar');
const permisos = document.querySelectorAll('input[type=checkbox]');

function habilitar(selected) {
    estado_checkbox = false;
    
    if (selected == 0) {
        submitButton.toggleAttribute('disabled', true);
        document.getElementById('desc_rol').toggleAttribute('disabled', true);
        estado_checkbox = true;      
    } else {
        submitButton.toggleAttribute('disabled', false);
        document.getElementById('desc_rol').toggleAttribute('disabled', false);
    }
    bloquear_checkbox(estado_checkbox);
    
    check_permiso = validar_checkbox();
    if (!check_permiso) {
        submitButton.toggleAttribute('disabled', true);
    } else {
        submitButton.toggleAttribute('disabled', false);
    }
   
}

function bloquear_checkbox(estado) {
    var i = 0;
    while (i < permisos.length) {      
        permisos[i].toggleAttribute('disabled', estado);
        i++;
    }
}

permisos.forEach((box) => {
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
    var i = 0;
    var al_menos_uno = false;   
    if (!estado_checkbox) {
        //Recorrido de checkbox's
        while (i < permisos.length) {
            // Verifica si esta checked
            if (permisos[i].checked) {
                al_menos_uno = true;             
                return al_menos_uno;
            }
            i++
        }       
    }else {
        return al_menos_uno;
    }  
}