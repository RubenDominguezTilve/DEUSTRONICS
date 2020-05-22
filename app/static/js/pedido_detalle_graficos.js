var ctx = document.getElementById("grafico").getContext("2d");
let color = "#1e90ff";
alert();
fetch(`../../api/estadisticas/pedido/${id_pedido}/`)
  .then(function (res) {
    console.log(res.text());
    if (res.ok) {
      return JSON.parse(res.text());
    } else {
      throw "Error desconocido";
    }
  })
  .then(function (data) {
    console.log(data);
  })
  .catch(function (error) {
    alertify.error("error");
  });

var chart = new Chart(ctx, {
  // The type of chart we want to create
  type: "doughnut",

  // The data for our dataset
  data: {
    labels: ["January", "February", "March", "April", "May", "June", "July"],
    datasets: [
      {
        label: "Progreso de pedido",
        backgroundColor: "#1e90ff",
        borderColor: color,
        data: [0, 10, 5, 2, 20, 30, 45],
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
function resize() {
  chart.canvas.parentNode.style.height = document.documentElement.clientHeight * 1 + "px";
  chart.canvas.parentNode.style.width = document.documentElement.clientWidth * 1 + "px";
}
