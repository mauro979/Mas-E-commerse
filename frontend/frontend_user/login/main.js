//seleccionando los elementos del front
const username = document.querySelector("#name-input");
const password = document.querySelector("#password-input");
const email = document.querySelector("#email");
const botonEnviar = document.querySelector("#Create-account-button");
const container = document.querySelector(".flex-container");
const carga = document.querySelector("#carga");

//agregandole la funcion al boton de crear para 
//comunicarnos con el backend

botonEnviar.addEventListener("click",()=>{
    if (username.value.length >  2 && password.value.length > 3 && email.value.length > 3 && email.value.includes("@")){
        container.style.display = "none";
        carga.style.display = "block";
        axios.post("http://127.0.0.1:8000/user/login",{ //poner la url
            "username" : username.value,
            "email" : email.value,
            "password" : password.value
        },{ withCredentials: true }).then(()=>{window.location.href = "http://127.0.0.1:5500/frontend/frontend_user/index.html"}).catch(()=>{
            container.style.display = "block";
            carga.style.display = "none";
            alert("por favor revice la informacion")});  
    }else{alert("por favor verifique la informacion introducida")};
});