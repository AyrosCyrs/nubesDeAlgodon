// static/inventario/main.js

console.log("☁️ nubesDeAlgodon cargado correctamente");

// Animación de bienvenida en consola
console.log("%c¡Bienvenida, Ayros! 🌸", "color: #5f9ea0; font-size: 16px; font-weight: bold;");

// Función para modo oscuro (usada en inicio.html)
function toggleDarkMode() {
    document.body.classList.toggle('dark-mode');
    console.log("Cambiando modo de luz/oscuridad...");
}

// Función para vender productos (usada en productos.html)
function vender(elemento) {
    let stockElement = elemento.querySelector('.stock');
    let cantidad = parseInt(stockElement.innerText);
    if (cantidad > 0) {
        stockElement.innerText = cantidad - 1;
        stockElement.style.color = (cantidad - 1 === 0) ? "red" : "green";
    }
}