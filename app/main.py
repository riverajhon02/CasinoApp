from fastapi import FastAPI
from app.api.routes import auth, users, centro_costo,empresa

app = FastAPI(title="Casino API")

# Rutas
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(centro_costo.router)
app.include_router(empresa.router)