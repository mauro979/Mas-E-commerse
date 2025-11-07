/*
 crear el js para enviarselos a esta url:     "http://127.0.0.1:8000/loginadmin"
*/

//seleccionando los elementos de el html
const username = document.querySelector("#name-input");
const password = document.querySelector("#password-input");
const email = document.querySelector("#email");
const botonEnviar = document.querySelector("#Create-account-button");
const container = document.querySelector(".flex-container");
const carga = document.querySelector("#carga");

botonEnviar.addEventListener("click",()=>{
    if (username.value.length > 2 && email.value.length > 4 && email.value.includes("@")){
        container.style.display = 'none';
        carga.style.display = 'block';
        axios.post("http://127.0.0.1:8000/loginadmin",{
        "username" : username.value,
        "email" : email.value,
        "password" : password.value,
    },{ withCredentials: true }
    ).then(()=>window.location.href = "http://127.0.0.1:5500/frontend/frontend_admin/panel/index.html").catch(()=>{
        carga.style.display = 'none';
        container.style.display = 'block';
        alert("por favor verifica la informacion")});
    }
    
})

/*
axios.get("http://127.0.0.1:8000/loginadmin",{
        "username" : username
    })
*/