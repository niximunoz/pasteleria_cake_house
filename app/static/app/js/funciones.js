

function validarCampos() {
    var rut = document.getElementById("txt-rut").value;
    var nom = document.getElementById("txt-nom").value;
    var apell = document.getElementById("txt-apell1").value;
    var apell = document.getElementById("txt-apell2").value;
    var correo = document.getElementById("correo").value;
    var pass = document.getElementById("pass").value;
    var fecha = document.getElementById("txt-fecha").value;
    var region = document.getElementById("region").value;
    var direccion = document.getElementById("txt-direccion").value;
    var numero = document.getElementById("txt-numero").value;



    if (rut.trim() == "") {
        document.getElementById("error-rut").style.visibility = "visible";
    }
    else {
        document.getElementById("error-rut").style.visibility = "hidden";

    }
    if (nom.trim() == "") {
        document.getElementById("error-nom").style.visibility = "visible"
    }
    else {
        document.getElementById("error-nom").style.visibility = "hidden";
    }
    if (apell.trim() == "") {
        document.getElementById("error-apell1").style.visibility = "visible"
    }
    else {
        document.getElementById("error-apell1").style.visibility = "hidden";
    }
    if (apell.trim() == "") {
        document.getElementById("error-apell2").style.visibility = "visible"
    }
    else {
        document.getElementById("error-apell2").style.visibility = "hidden";
    }
    if (apell.trim() == "") {
        document.getElementById("error-correo").style.visibility = "visible"
    }
    else {
        document.getElementById("error-correo").style.visibility = "hidden";
    }
    if (apell.trim() == "") {
        document.getElementById("error-pass").style.visibility = "visible"
    }
    else {
        document.getElementById("error-pass").style.visibility = "hidden";
    }
    if (direccion.trim() == "") {
        document.getElementById("error-direccion").style.visibility = "visible";
    }
    else {
        document.getElementById("error-direccion").style.visibility = "hidden";
    }
    if (numero.trim() == "") {
        document.getElementById("error-numero").style.visibility = "visible";
    }
    else {
        document.getElementById("error-numero").style.visibility = "hidden";
    }
}
function checkRut(rut) {
    // Despejar Puntos
    var valor = rut.value.replace('.', '');
    // Despejar Guión
    valor = valor.replace('-', '');

    // Aislar Cuerpo y Dígito Verificador
    cuerpo = valor.slice(0, -1);
    dv = valor.slice(-1).toUpperCase();

    // Formatear RUN
    rut.value = cuerpo + '-' + dv

    // Si no cumple con el mínimo ej. (n.nnn.nnn)
    if (cuerpo.length < 7) { rut.setCustomValidity("RUT Incompleto"); return false; }

    // Calcular Dígito Verificador
    suma = 0;
    multiplo = 2;

    // Para cada dígito del Cuerpo
    for (i = 1; i <= cuerpo.length; i++) {

        // Obtener su Producto con el Múltiplo Correspondiente
        index = multiplo * valor.charAt(cuerpo.length - i);

        // Sumar al Contador General
        suma = suma + index;

        // Consolidar Múltiplo dentro del rango [2,7]
        if (multiplo < 7) { multiplo = multiplo + 1; } else { multiplo = 2; }

    }

    // Calcular Dígito Verificador en base al Módulo 11
    dvEsperado = 11 - (suma % 11);

    // Casos Especiales (0 y K)
    dv = (dv == 'K') ? 10 : dv;
    dv = (dv == 0) ? 11 : dv;

    // Validar que el Cuerpo coincide con su Dígito Verificador
    if (dvEsperado != dv) { rut.setCustomValidity("RUT Inválido"); return false; }

    // Si todo sale bien, eliminar errores (decretar que es válido)
    rut.setCustomValidity('');
}