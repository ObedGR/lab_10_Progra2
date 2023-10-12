function validarFormulario() {
    var Titulo = document.getElementById("Titulo").value;
    var Autor = document.getElementById("Autor").value;
    var Editorial = document.getElementById("Editorial").value;
    var Paginas = document.getElementById("Paginas").value;
    var Publicacion = document.getElementById("Anio").value;
    var ISBN = document.getElementById("ISBN").value;

    var error = document.getElementById("js-Error");

    if (Titulo == "" || Autor == "" || Editorial == "" || Paginas == "" || Publicacion == "" || ISBN == "") {
        error.style.display = "block";
        return false;
    }
    else{
        error.style.display = "none";
        return true;
    }
}

document.getElementById("formulario").onsubmit = function (event) {
    if(!validarFormulario()){
        event.preventDefault();
    }
};