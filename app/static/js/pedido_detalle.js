
document.getElementById("elBoton").addEventListener("click", function(event){
    event.preventDefault()

    //Definimos el formulario para luego acceder a sus datos
    let form = document.getElementById("formNuevaTarea");
    //Definimos la tarea para luego añadirla a BBDD
    let tarea = new FormData(form);
    //Llamada AJAX 
    tarea.append("csrfmiddlewaretoken", csrftoken);


    //Hasta aqui parece coherente
    fetch("../../añadirTarea/", {
      method: "POST",
      body: tarea,
    })
      .then(function (response) {
        if (response.ok) {
          return response.text();
        } else {
          throw "Error en la llamada Ajax";
        }
      })
      .catch(function (err) {
        alertify.error("error inesperado");
      });


  });


