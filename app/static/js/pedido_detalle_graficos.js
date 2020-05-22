var ctx = document.getElementById("grafico").getContext("2d");
let color1 = "#1e90ff";
let color2 = "#a4b0be";
var chart;
fetch(`../../api/estadisticas/pedido/${id_pedido}/`)
  .then(function (res) {
    console.log(res);
    if (res.ok) {
      return res.json();
    } else {
      throw "Error desconocido";
    }
  })
  .then(function (data) {
    console.log("data 14");
    console.log(data);
    data.pendientes = data.pendientes == 0 ? 1 : data.pendientes;
    let datos = [data.realizadas, data.pendientes];
    console.log(datos);
    chart = new Chart(ctx, {
      // The type of chart we want to create
      type: "doughnut",

      // The data for our dataset
      data: {
        labels: ["Realizadas", "Planificadas"],
        datasets: [
          {
            label: "Progreso de pedido",
            backgroundColor: [color1, color2],
            borderColor: [color1, color2],
            data: datos,
          },
        ],
      },

      // Configuration options go here
      options: {
        responsive: true,
      },
    });

    resize();
    window.addEventListener("resize", resize);
  })
  .catch(function (error) {
    alertify.error("error");
  });

function resize() {
  chart.canvas.parentNode.style.height = document.documentElement.clientHeight * 1 + "px";
  chart.canvas.parentNode.style.width = document.documentElement.clientWidth - 20 + "px";
}
