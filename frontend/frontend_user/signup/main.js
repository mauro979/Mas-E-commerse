//seleccionando los elementos del frontend
const boton_enviar = document.getElementById("Create-account-button");
const nombre = document.getElementById("name-input");
const email = document.getElementById("email");
const password = document.getElementById("password-input");
const contenedor = document.querySelector(".crear-cuenta-container") 
const carga = document.getElementById('carga')

boton_enviar.addEventListener("click",()=>{

    if(
        nombre.value.length > 4 && 
        email.value.includes("@") &&
        password.value.length > 5
    ){

        contenedor.style.display = 'none';
        carga.style.display = 'block';

        axios.post("http://127.0.0.1:8000/CreateAccountUser",{
        "username" : nombre.value,
        "email" : email.value,
        "password" : password.value,
        "admin" : false
    },
    { withCredentials: true }
    ).then(()=>window.location.href = "http://127.0.0.1:5500/frontend/frontend_user/index.html")
    .catch()}else{console.log(alert("por favor verifique la informacion introducida"))};
});

//window.location.href = "http://127.0.0.1:5500/frontend/frontend_user/index.html"