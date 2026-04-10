from fastapi import FastAPI
from app.api.routes import auth, users, centro_costo, empresa, perfil_usuario
import app.db.base  

app = FastAPI(title="Casino API")

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(centro_costo.router)
app.include_router(empresa.router)
app.include_router(perfil_usuario.router)

@app.get("/test-directo")
def test():
    return {"status": "ok"}