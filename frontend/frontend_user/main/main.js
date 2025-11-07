// axios.get("http://127.0.0.1:8000/tokenverification",
//     { withCredentials: true }
// ).then(response =>{
//     console.log("perfecto")})
// .catch(response => {if (response.request.status == 401 || response.request.status == 406){
//     window.location.href = "http://127.0.0.1:5500/frontend/frontend_user/login/index.html"
// }})
// .catch(response => {console.log(response.request.status)})
        //response.request.statusText == "Unauthorized"
        //http://127.0.0.1:5500/frontend/frontend_user/index.html



        //## solicitud cantidad de productos en stock ## 

let cantidadDeProductos = null;
                        
//seleccionando los elementos del documento html
const productosContenedor = document.querySelector("#products-flex-container");
const body = document.querySelector("body");
//---------------------------------------------------------------------------------

const framentoDocumentoTesting = document.createDocumentFragment();

axios.get("http://127.0.0.1:8000/productos/cantidad").then((response)=>{
        axios.get(`http://127.0.0.1:8000/productos/chakepoint/${Number(response.data.cantidad)}`).then((response) =>{

                for (let i= 0; i < response.data.productos.length; i++){
                        const contenedorProducto = document.createElement("div");
                        contenedorProducto.className = 'producto-modelo-agregar';
                        contenedorProducto.id = response.data.productos[i]._id;

                        const imgenProducto = document.createElement("div");
                        imgenProducto.style.backgroundImage = `url("data:image/png;base64,${response.data.productos[i].image}")`;
                        imgenProducto.className = 'producto-modelo-agregar-imagen';

                        const nombreProducto = document.createElement("h2");
                        nombreProducto.textContent = String(response.data.productos[i].name);
                        nombreProducto.className = 'producto-modelo-agregar-titulo';

                        const descripcionProducto = document.createElement("p");
                        descripcionProducto.textContent = String(response.data.productos[i].description);
                        descripcionProducto.className = 'producto-modelo-agregar-descripcion';

                        const precioProducto = document.createElement("h5");
                        precioProducto.textContent = `${String(response.data.productos[i].price)}`;
                        precioProducto.className = 'producto-modelo-agregar-precio';
                        
                        const stockProducto = document.createElement("h6")
                        stockProducto.textContent = `Disponibilidad: ${Number(response.data.productos[i].stock)}`;
                        stockProducto.className = 'producto-modelo-agregar-stock';

                        //agregandolos todos al contenedor del producto
                        contenedorProducto.appendChild(imgenProducto);
                        contenedorProducto.appendChild(nombreProducto);
                        contenedorProducto.appendChild(descripcionProducto);
                        contenedorProducto.appendChild(precioProducto);
                        contenedorProducto.appendChild(stockProducto);

                        //agregandolos al document fragment
                        
                        framentoDocumentoTesting.appendChild(contenedorProducto);

        };productosContenedor.appendChild(framentoDocumentoTesting);}).catch((err)=>{if(err.request.status === 404){alert("por ahora no hay productos disponibles")}})
})