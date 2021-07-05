$(document).ready(function () {
    $.getJSON('https://mindicador.cl/api', function (data) {
        var indicadores = data;
        $("#dolar").text("Dolar: $"+indicadores.dolar.valor)
    }).fail(function () {
        console.log('Error al consumir la API!');
    });
});
