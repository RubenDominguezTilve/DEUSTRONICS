var datajson;
function lista_productos(data) {
  let cad = "";
  console.log(data);
  for (let element of data) {
    cad += `<p>${element.nombre}</p>`;
  }
  return cad;
}

fetch("../api/catalogo")
  .then(function (response) {
    if (response.ok) {
      return response.text();
    } else {
      throw "Error en la llamada Ajax";
    }
  })
  .then(function (data) {
    document.getElementsByClassName("MultiCarousel-inner")[0].innerHTML = lista_productos(JSON.parse(data));
    console.log(data);
  })
  .catch(function (error) {
    console.log(error);
  });
