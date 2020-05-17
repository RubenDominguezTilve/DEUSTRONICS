var datajson;
function lista_productos(data) {
  let cad = "";
  console.log(data.length);

  for (let i = 0; i < data.length; i++) {
    cad += template_catalogo(data[i], i);
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

function template_catalogo(producto, i) {
  return ` 
      <div class="item catalog-item mb-2 col-sm-3" style="animation-delay:${0.2 * i}s;" >
      <div class="pad15">
        <!-- Imagen del producto -->
        <img src="https://dummyimage.com/600x400/000/fff" class="img-fluid rounded mx-auto d-block" alt="Imagen de catálogo" />
        <!-- Nombre del producto -->
        <p class="lead mt-2">${producto.nombre}</p>
        <!-- Descripción del producto 
        <p>Descripción: ${producto.descripcion}</p>-->
        <!-- Detalle del producto -->
        <a href="${producto.id}"> Ver detalle</a>
        <!-- Precio del producto por unidad -->
        <p>Precio: ${producto.precio} €</p>
        




        <!-- Cantidad de unidades a pedir -->
        <div class="input-group mb-3">
          <form  action="../pedido/create/" method="POST">
         
            <input type="hidden" name="csrfmiddlewaretoken" value="${csrftoken}">
            <span class="input-group-text FormGroupPedido" >Cantidad</span>
            
            <input type="hidden" name="producto" value="${producto.id}" />
            <input type="number" class="form-control FormGroupPedido" aria-label="Sizing example input"
              aria-describedby="inputGroup-sizing-default" name="cantidad" />
            <!-- Apéndice para el botón de realizar pedido -->
            <button class="btn btn-outline-dark bg-secondary FormGroupPedido" type="submit" id="button-addon1">Pedir</button>
            
            <hr>
           
            <p>Precio total: <span>${producto.precio}</span> €</p>
          </form>
        </div>       
      </div>
    </div>`;
}
