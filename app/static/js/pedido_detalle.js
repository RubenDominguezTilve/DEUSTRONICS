document.getElementById("elBoton").addEventListener("click", function (event) {
  event.preventDefault();

  //Definimos el formulario para luego acceder a sus datos
  let form = document.getElementById("formNuevaTarea");
  //Definimos la tarea para luego añadirla a BBDD
  let tarea = new FormData(form);
  //Llamada AJAX
  tarea.append("csrfmiddlewaretoken", csrftoken);
  let equiposel = document.querySelector("[name=equipo]");
  let procesosel = document.querySelector("[name=proceso]");
  var datos = {
    equipo: equiposel.options[equiposel.selectedIndex].text,
    proceso: procesosel.options[procesosel.selectedIndex].text,
  };
  console.log(datos);
  //Hasta aqui parece coherente
  fetch("../../api/anadirTarea/", {
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
    .then(function (text) {
      console.log(text);

      datos.id = text;
      datos.hora_inicio = tarea.get("hora_inicio");
      datos.hora_fin = tarea.get("hora_fin");
      anadir_row(datos);
      alertify.success("Añadido correctamente");
    })
    .catch(function (err) {
      console.log(err);
      alertify.error("error inesperado");
    });
});

// function template_tarea(tarea) {
//   return `
//   <tr>
//     <td>${tarea.get("proceso")}</td>
//     <td>${tarea.get("equipo")}</td>
//     <td>${tarea.get("pedido")}</td>
//     <td>${tarea.get("hora_inicio")}</td>
//     <td>${tarea.get("hora_fin")}</td>
//     <td><a href="/tarea/${tarea.get("id")}">Ver detalle</a></td>
// </tr>`;
// }

function anadir_row(tarea) {
  var table = document.getElementById("tareas-body");

  var row = table.insertRow(-1); //si le pones un -1 lo pone al final
  var cell0 = row.insertCell(0);
  var cell1 = row.insertCell(1);
  var cell2 = row.insertCell(2);
  var cell3 = row.insertCell(3);
  var cell4 = row.insertCell(4);

  cell0.innerHTML = tarea.proceso;
  cell1.innerHTML = tarea.equipo;
  cell2.innerHTML = tarea.hora_inicio;
  cell3.innerHTML = tarea.hora_fin;
  cell4.innerHTML = `<a href="/tarea/${tarea.id}">Ver detalle</a>`;
}
