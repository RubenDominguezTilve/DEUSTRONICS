var esCliente;


var datajson;
function lista_productos(data) {
  let cad = "";

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
    datos = JSON.parse(data);
    esCliente = datos.cliente;
    document.getElementById("productos-catalogo").innerHTML = lista_productos(datos.productos);
    
    
    var inputsCantidad = document.getElementsByClassName("inputCantidad");
    for (var i = 0; i < inputsCantidad.length; i++) {
      inputsCantidad[i].addEventListener("change", function (event) {
        let newValue = event.target.value;
        let form = event.target.parentNode;
        let pedido = new FormData(form);
        let nuevoPrecioTotal = newValue * pedido.get("precio");
        //Recorremos el arbol para cambiar el valor del Span
        let siguiente = form.nextElementSibling;
        //HASTA AQUI TODO OK HORSELUIS siguiente ES PARRAFO <p>
        let hijosiguiente = siguiente.children[0];
        //HIJOSIGUIENTE ES EL SPAN
        hijosiguiente.innerHTML = nuevoPrecioTotal;
      }
      );
    }
  })
  .catch(function (error) {
    console.log(error);
  });

function template_catalogo(producto, i) {
  
  console.log("Producto: " + producto);
  console.log("Producto.imagen: " + producto.imagen);
  console.log("Producto.imagen.url: " + producto.imagen.url);
  //console.log("Producto.imagen.url.bien?: " /media/+ producto.imagen); 

  retorno = ` 
  <div class="item catalog-item mb-2 col-sm-3"  >
  <div class="pad15">
    <!-- Imagen del producto -->
    <img src="/media/${producto.imagen}" class="img-fluid rounded mx-auto d-block" alt="Imagen de catálogo" />
    <!-- Nombre del producto -->
    <p class="lead mt-2">${producto.nombre}</p>
    <!-- Descripción del producto 
    <p>Descripción: ${producto.descripcion}</p>-->
    <!-- Detalle del producto -->
    <a href="${producto.id}"> Ver detalle</a>
    <!-- Precio del producto por unidad -->
    <p>Precio: ${producto.precio} €</p>
    `

    
    if (esCliente){
      retorno +=
      `
    <!-- Cantidad de unidades a pedir -->
    <div class="input-group mb-3">
      <form  action="../pedido/create/" method="POST">
     
        <input type="hidden" name="csrfmiddlewaretoken" value="${csrftoken}">
        <span class="input-group-text FormGroupPedido" >Cantidad</span>
        
        <input type="hidden" name="producto" value="${producto.id}" />
        <input type="hidden" name="precio" value="${producto.precio}" />
        <input type="number" class="form-control FormGroupPedido inputCantidad" aria-label="Sizing example input"
          aria-describedby="inputGroup-sizing-default" name="cantidad" value="1" min="0"/>
        <!-- Apéndice para el botón de realizar pedido -->
        <button class="btn btn-outline-dark bg-secondary FormGroupPedido" type="submit" id="button-addon1">Pedir</button>
        
        <hr>
       
      </form>
      <p class="mx-auto">Precio total: <span>${producto.precio}</span> €</p>
    </div>  
    `
    } 

    retorno += `
    </div>
    </div>`
    ;



  return retorno
}


