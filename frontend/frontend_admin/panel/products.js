//seleccionando los elementos del documento

const imagenDiv = document.querySelector(".imagen");
const logoDiv = document.querySelectorAll(".logo");  //si se va la luz aqui tienes pq no funciona, cambialo por el queryselector y ya
const addImage = document.getElementById("fileInput");

//seleccionando elementos de el producto modelo

const botonCrear = document.getElementById("Crear");
const nombreDelProducto = document.querySelector(".producto-modelo-agregar-titulo");
const descripcionDelProducto = document.querySelector(".producto-modelo-agregar-descripcion");
const precioDelProducto = document.querySelector(".producto-modelo-agregar-precio");
const disponibilidadDelProducto = document.querySelector(".producto-modelo-agregar-stock");
const nombreDelProductoP = document.getElementById("Nombre-producto-content");

//selecccionando los elementos de la seccion de eliminacion de productos
const sectionEliminarProducto = document.querySelector("#eliminar-productos");
const inputEliminarProductos = document.getElementById("input-buscar-producto-para-eliminar");
const botonBuscarProductos = document.getElementById("boton-buscar-producto-para-eliminar");
const eliminarProductoImagen = document.querySelector("#eliminar-producto-imagen");
const tituloEliminarProducto = document.querySelector(".producto-modelo-eliminar-titulo");
const productoEliminarDescripcion = document.querySelector(".producto-modelo-eliminar-descripcion");
const productoEliminarPrecio = document.querySelector(".producto-modelo-eliminar-precio");
const productoEliminarStock = document.querySelector(".producto-modelo-eliminar-stock");
const productoEliminarModeloContainer = document.getElementById("modelo-producto-eliminar-container");
const eliminarProductoBoton = document.querySelector("#Eliminar");

//definiendo las funciones
const convertirBase64AImagen = (base64String,div) => {
    // Crear un objeto Image
    const imagenDesencriptada = new Image();

    // Asignar el src con el encabezado adecuado
    imagenDesencriptada.src = "data:image/png;base64," + base64String;

    // Retornar la imagen para poder usarla fuera si se necesita
    // div.appendChild(imagenDesencriptada);
    div.style.backgroundImage = `url(${imagenDesencriptada.src})`
}


//haciendo las peticiones
    
axios.get("http://127.0.0.1:8000/logo").then((response)=>
    {const logoResponse = response.data.logo
    logoDiv.forEach((div)=>{convertirBase64AImagen(logoResponse,div)})
    convertirBase64AImagen(logoResponse,imagenDiv)}
).catch((err)=>{if(err.request.status === 424){alert("algo a salido mal :(")}})

let encriptImageProduct = null;

addImage.addEventListener("change", function(event) {
    const file = event.target.files[0];
    if (!file) return;

    const reader = new FileReader();

    reader.onload = function(e) {
        const dataUrl = e.target.result; // Esto es una URL base64
        imagenDiv.style.backgroundImage = `url(${dataUrl})`;

        const base64String = dataUrl.split(',')[1];
        encriptImageProduct = base64String;

    };

    reader.readAsDataURL(file);
});


//enviando los datos del nuavo producto al backend y verificando q el administrador sea realmente el administrador
botonCrear.addEventListener("click", ()=>{
    axios.get("http://127.0.0.1:8000/tokenverificationadmin",
        { withCredentials: true }
    ).then(()=>
        axios.post("http://127.0.0.1:8000/createproducts",{                                         
            "name" : nombreDelProducto.textContent,
            "price" : precioDelProducto.textContent,
            "description" : descripcionDelProducto.textContent,
            "image" : String(encriptImageProduct),
            "stock" : disponibilidadDelProducto.textContent
        })
        .then((response)=>{if(response.request.status == 201){alert("Producto creado con exito")}})
        .catch((err)=>{if(err.request.status === 409){alert("El producto ya existe")}})

    ).catch((err)=>{if(err.request.status === 406 || err.request.status === 409){alert("algo a salido mal :(")};window.location.href = "http://127.0.0.1:5500/frontend/frontend_admin/login/index.html"});
})

let idDelProducto = null;

//agregandole la funcion a el boton de buscar de enviarle al back el nombre del producto
botonBuscarProductos.addEventListener("click", () => {
    axios.get("http://127.0.0.1:8000/tokenverificationadmin",
    { withCredentials: true }
).then( () =>
    axios.get(`http://127.0.0.1:8000/productos/buscarpornombre/${(inputEliminarProductos.value)}`).then((response)=>
        {productoEliminarModeloContainer.style.display = "flex";
        convertirBase64AImagen(response.data.data.image,eliminarProductoImagen);
        console.log(response.data.data.name);
        tituloEliminarProducto.textContent = String(response.data.data.name);
        productoEliminarPrecio.textContent = String(response.data.data.price);
        productoEliminarStock.textContent = String(response.data.data.stock);
        productoEliminarDescripcion.textContent = String(response.data.data.description);
        idDelProducto = response.data.data.id;
        console.log(idDelProducto)}

    ).catch((response)=>{if (response.status == 404){alert(response.statusText)}})
).catch((error) => {
    if (error.response && (error.response.status === 401 || error.response.status === 406)) {
      window.location.href = "http://127.0.0.1:5500/frontend/frontend_admin/login/index.html";
    }
})})

eliminarProductoBoton.addEventListener("click",()=>{
axios.get("http://127.0.0.1:8000/tokenverificationadmin",
    { withCredentials: true }
).then(() => {
    axios.delete(`http://127.0.0.1:8000/productos/delete/${idDelProducto}`).then(() => {productoEliminarModeloContainer.style.display = "none";alert("Producto eliminado con exito")}).catch(()=>alert("El producto no existe"))
}).catch((error) => {
    if (error.response && (error.response.status === 401 || error.response.status === 406)) {
      window.location.href = "http://127.0.0.1:5500/frontend/frontend_admin/login/index.html";
}})})