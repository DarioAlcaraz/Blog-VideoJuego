// Este script muestra un mensaje en la consola y en pantalla
console.log("¡scripts.js cargado correctamente!");

document.addEventListener("DOMContentLoaded", function () {
  const saludo = document.createElement("div");
  saludo.textContent = "¡Bienvenido al blog gamer!";
  saludo.style.position = "fixed";
  saludo.style.bottom = "20px";
  saludo.style.right = "20px";
  saludo.style.backgroundColor = "#212529";
  saludo.style.color = "#fff";
  saludo.style.padding = "10px 20px";
  saludo.style.borderRadius = "8px";
  saludo.style.boxShadow = "0 0 10px rgba(0,0,0,0.5)";
  saludo.style.zIndex = "1000";

  document.body.appendChild(saludo);

  setTimeout(() => {
    saludo.remove();
  }, 4000); // Se borra después de 4 segundos
});