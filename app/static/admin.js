document.addEventListener("DOMContentLoaded", function () {

    const reemplazos = {
        "List": "Lista",
        "Create": "Crear",
        "Add Filter": "Agregar filtro",
        "With selected": "Acciones",
        "Search": "Buscar"
    };

    document.querySelectorAll("a, button").forEach(el => {
        const texto = el.innerText.trim();
        if (reemplazos[texto]) {
            el.innerText = reemplazos[texto];
        }
    });

});