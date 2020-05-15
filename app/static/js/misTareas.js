var checks = document.getElementsByClassName("check-finalizar");

for (var i = 0; i < checks.length; i++) {
  checks[i].addEventListener("click", function (event) {
    let form = event.target.parentNode;
    console.log(form);
    let tarea = new FormData(form);
    console.log(tarea.get("idtarea"));
    let row = form.parentNode.parentNode;
    row.classList.add("tarea-done");

    setTimeout(function () {
      row.remove();
    }, 2000);
  });
}
