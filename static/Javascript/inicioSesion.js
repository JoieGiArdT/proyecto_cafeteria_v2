function validacion() {
    var usuario = document.formulario.Nombre;
    var contraseña = document.formulario.Pass;

    var longitud_usuario = usuario.value.length;
    if (longitud_usuario < 5) {
        alert("Debe ingresar minimo 5 caracteres");
    }

    var longitud_contraseña = contraseña.value.length;
    if (longitud_contraseña < 8) {
        alert("Debe ingresar minimo 8 caracteres");
    }

};

function mostrarPassword() {
    var mostrar = document.getElementById('userPassword');
    mostrar.type = "text";

}

function ocultarPassword() {
    var ocultar = document.getElementById('userPassword');
    ocultar.type = "password";
}