from fastapi import FastAPI
from app.api.routes import auth, users, centro_costo, empresa, perfil_usuario, proteina
import app.db.base  
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Casino API")


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(centro_costo.router)
app.include_router(empresa.router)
app.include_router(perfil_usuario.router)
app.include_router(proteina.router)

@app.get("/test-directo")
def test():
    return {"status": "ok"}