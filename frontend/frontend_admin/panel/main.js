//verificando si el token de acceso es correcto
axios.get("http://127.0.0.1:8000/tokenverificationadmin",
    { withCredentials: true }
).then(response =>{
    console.log("perfecto")})
.catch(response => {if (response.request.status == 401 || response.request.status == 406){
    window.location.href = "http://127.0.0.1:5500/frontend/frontend_admin/login/index.html"
}})

//seleccionando los elementos del DOM
const abrirNavBar = document.querySelector(".boton-menu-desplegable");
const navBar = document.querySelector("#navbar");



abrirNavBar.addEventListener("click", () => {
    // transiciones
    abrirNavBar.style.transition = "transform 200ms ease";
    navBar.style.transition = "opacity 200ms ease, transform 200ms ease";

    const currentDisplay = getComputedStyle(navBar).display;

    if (currentDisplay === "none") {
        // abrir: primero hacemos visible y animamos desde arriba con opacidad 0 -> 1

        navBar.style.display = "flex";
        navBar.style.opacity = "0";
        navBar.style.transform = "translateY(-10px)";

        // forzar reflow para que la transición funcione
        void navBar.offsetWidth;

        navBar.style.opacity = "1";
        navBar.style.transform = "translateY(0)";
        abrirNavBar.style.transform = "rotate(90deg)";
    } else {
        // cerrar: animar opacidad y luego ocultar al terminar la transición
        navBar.style.opacity = "0";
        navBar.style.transform = "translateY(-10px)";
        abrirNavBar.style.transform = "rotate(0deg)";

        const onTransitionEnd = (e) => {
            if (e.propertyName === "opacity") {
                navBar.style.display = "none";
                navBar.removeEventListener("transitionend", onTransitionEnd);
            }
        };
        navBar.addEventListener("transitionend", onTransitionEnd);
    }
});

// ...existing code...
const header = document.querySelector('header');

function adjustNavBarPosition() {
    if (!navBar) return;
    const isWide = window.innerWidth > 820;

    if (isWide && header) {
        navBar.style.left = '0';
        // usar margin-top igual a la altura del header
        navBar.style.marginTop = `${header.offsetHeight}px`;
        // ajustar altura para que no sobresalga debajo del footer (opcional)
        navBar.style.height = `calc(100vh - ${header.offsetHeight}px)`;
        navBar.style.zIndex = '1000';
    } else {
        // restaurar estilos por defecto cuando la pantalla es pequeña
        navBar.style.position = '';
        navBar.style.left = '';
        navBar.style.marginTop = '';
        navBar.style.height = '';
        navBar.style.zIndex = '';
    }
}

// ejecutar al cargar y al redimensionar
window.addEventListener('load', adjustNavBarPosition);
window.addEventListener('resize', adjustNavBarPosition);
// ...existing code...