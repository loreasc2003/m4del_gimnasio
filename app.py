from fastapi import FastAPI
from routes.user import user
from routes.person import person
from routes.rol import rol
from routes.usersrols import userrol
from routes.evaluacion_serv import evaluaciones_serv_router
from routes.pedidos import pedido_router
from routes.promociones import promocion_router

app = FastAPI()
app.include_router(user)
app.include_router(person)
app.include_router(rol)
app.include_router(userrol)
app.include_router(evaluaciones_serv_router)
app.include_router(pedido_router)
app.include_router(promocion_router)
