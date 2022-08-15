


document.addEventListener("DOMContentLoaded", function(e) {
   /*
    var agregarProducto = document.getElementsByClassName("btn btn-outline-primary");
    console.log(agregarProducto);
    
    for (let i = 0; i < agregarProducto.length; i++) {
        agregarProducto[i].addEventListener("click", (e)=>{
            console.log("asfasf");
    
        });
    }
*/


   
});



/*
document.getElementsByName("formulario")[0].addEventListener("submit", (e) => {
    e.preventDefault();
    let nombre = document.getElementsByName("formulario")[0].nombre.value;
    let descuento = document.getElementsByName("formulario")[0].descuento.value;
    let precio = document.getElementsByName("formulario")[0].precio.value;
    let imagen = document.getElementsByName("formulario")[0].imagen.value;
    let cantidad = document.getElementsByName("formulario")[0].cantidad.value;
    let objeto  = {
        nombre : nombre,
        descuento : descuento,
        precio : precio,
        imagen : imagen,
        cantidad : cantidad
    };

    arreglo.push(objeto);
    cargarTabla();
    guardarLocalStorage();

});


function cargarTabla() {
    var tabla = `<tr>
                    <th>Nombre</th>
                    <th>Descuento</th>
                    <th>Precio</th>
                    <th>Cantidad</th>
                    <th>Imagen</th>
                    <th>Total</th>
                </tr>`;
        
    var a = 0;
    for (let i = 0; i < arreglo.length; i++) {

        a = (arreglo[i].precio * arreglo[i].cantidad);
        tabla += "<tr>";
        tabla += "<td>"+arreglo[i].nombre+"</td>";
        tabla += "<td>"+arreglo[i].descuento+"</td>";
        tabla += "<td>"+arreglo[i].precio+"</td>";
        tabla += "<td>"+arreglo[i].cantidad+"</td>";
        tabla += "<td>"+arreglo[i].imagen+"</td>";
        tabla += "<td>"+a+"</td>";
        tabla +='</tr>';

    }
    document.getElementById("tablaProductos").innerHTML = tabla;
}


function guardarLocalStorage () {
    localStorage.setItem('CarritoCompra', JSON.stringify(arreglo));
}

function cargarLocalStorage () {
    if (localStorage.getItem('carrito') !== null) {
        arreglo = JSON.parse(localStorage.getItem('CarritoCompra'));
    }
}
*/