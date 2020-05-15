var checks = document.getElementsByClassName("check-finalizar");

//Recorremos todos los checkbox que tengan class="check-finalizar" (uno por tarea, en principio)
for (var i = 0; i < checks.length; i++) {
  //Añadimos un EventListener para poder saber cuando se clica el checkbox
  checks[i].addEventListener("click", function (event) {
    //Definimos el formulario para luego acceder a sus datos
    let form = event.target.parentNode;
    //Definimos la tarea para luego actualizarla en BBDD
    let tarea = new FormData(form);
    //Definimos las fila que corresponde a la tarea para despues eliminarla
    let row = form.parentNode.parentNode;
    //La marcamos como done, lo que la hace moverse via CSS
    row.classList.add("tarea-done");

    //Definimos el tiempo que se va a desplazar antes de eliminarla
    setTimeout(function () {
      row.remove();
    }, 2000);
  });
}
