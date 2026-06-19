from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controladores.UsuarioControlador import router as usuario_router

app = FastAPI(
    title="API del Sistema de Restaurante",
    description="Backend de producción para la app de React",
    version="1.0.0"
)

# Configuración de CORS para producción
# Reemplaza con la URL real de tu frontend en producción
origins = [
    "http://localhost:5173",  # React en desarrollo
    "https://mi-restaurante.vercel.app"  # React en producción
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrar las rutas del controladores
app.include_router(usuario_router)

# Para ejecutar en producción usarías en la terminal:
# uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4