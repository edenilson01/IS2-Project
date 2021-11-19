const fecha_1 = document.getElementById('fecha1');
const fecha_2 = document.getElementById('fecha2');

const calcularFecha =()=>{
    var sFecha =fecha_1.value;
    var aFecha = sFecha.split("-");
    var Fecha = new Date(aFecha[0], aFecha[1], aFecha[2]);
    var dias = duracion*7 //los dias que quieres aumentar
    var milisegundos = Fecha.getTime();
    Fecha.setTime( milisegundos + (dias * 86400000) );
    //Fecha.setTime(Fecha.getTime()+dias*24*60*60*1000); 
    Fecha= Fecha.getFullYear()+"-"+(Fecha.getMonth())+"-"+Fecha.getDate();
    return Fecha
}




window.addEventListener('load',function(){
    fecha_1.addEventListener("change", function() {
       // document.getElementById("reset_form").remove()

        if(this.value){
            if(duracion > 0){
                fecha_2.disabled;
                fech= calcularFecha();
                fecha_2.value = fech;
                fecha_2.placehorlder=fech;
            }
            
        }
    });

});

function habilitar(selected) {
    duracion = selected;
    fecha_1.value = "";
    fecha_2.value = "";
    fecha_1.disabled = true; 
    fecha_2.disabled = true; 
    if (duracion == 0) {
        fecha_1.disabled = false; 
        fecha_2.disabled = false;
    } else {

        if(duracion > 0 ) {
            fecha_1.disabled = false;
            fecha_2.disabled = true;
      
        }else{
            fecha_1.disabled = true;
            fecha_2.disabled = true;
        }
    }
}


