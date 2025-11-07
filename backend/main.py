from fastapi import FastAPI
from admin.routers.login.create_account_admin import router
from verificacion import router as verificacion_router
from fastapi.middleware.cors import CORSMiddleware
from admin.routers.panel.agg_product import router as add_product_router
from user.routers.agg_user import router as add_user
from admin.routers.panel.interfaz import router as interfaz_router
from tokenverificationadmin import router as router_verification_token
from admin.routers.panel.buscar_por_nombre_productos import router as buscar_producto_por_nombre_router 
from admin.routers.panel.eliminar_productos import router as router_eliminar_productos
from admin.routers.login.login import router as login_admin_router
from user.routers.login import router as login_user_ruter
from user.routers.cantidad_productos import router as cantidad_de_productos_router
from user.routers.products import router as products_router
from user.routers.products_info import router as router_info_productos

app = FastAPI()

#routers generales
app.include_router(verificacion_router)

#routers de administrador
app.include_router(login_admin_router)
app.include_router(router)
app.include_router(add_product_router)
app.include_router(interfaz_router)
app.include_router(router_verification_token)
app.include_router(buscar_producto_por_nombre_router)
app.include_router(router_eliminar_productos)

#routeres de usuario
app.include_router(add_user)
app.include_router(login_user_ruter)
app.include_router(cantidad_de_productos_router)
app.include_router(products_router)
app.include_router(router_info_productos)
 
# Lista de orígenes permitidos
origins = [
    "http://127.0.0.1:8000",
    "http://127.0.0.1:5500",
    "http://127.0.0.1:5500/frontend_user/index.html",
    "http://127.0.0.1:5500/tokenverification",
    "http://127.0.0.1:5500/frontend/frontend_admin/login/index.html",
    "http://127.0.0.1:5500/frontend/frontend_user/login/index.html",    
    "http://127.0.0.1:5500/frontend/frontend_admin/panel/index.html",
    "http://127.0.0.1:8000/productos/delete/"
    "http://127.0.0.1:8000/loginadmin",
    "http://127.0.0.1:5500/frontend/frontend_admin/login/index.html",
    "http://127.0.0.1:5500/frontend/frontend_admin/createAccount/index.html",
    "http://127.0.0.1:5500/frontend/frontend_user/login/index.html",

]

# Configurar el middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,              # Solo estos orígenes pueden acceder
    allow_credentials=True,
    allow_methods=["*"],                # Puedes restringir si lo deseas
    allow_headers=["*"]                 # Puedes especificar headerjs permitidos
)