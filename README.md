# Sistema de Restaurante — Guía de Laboratorio #04

Aplicación fullstack para la gestión de un restaurante, desarrollada como parte del curso **Desarrollo de Software I** de la UNSAAC.

## Arquitectura

```
app-Restauranteguia5/
├── AppRestaurante/      ← Backend (Python + FastAPI)
└── sistemarestaurante/  ← Frontend (React + TypeScript + Vite)
```

## Backend — `AppRestaurante/`

| Tecnología | Uso |
|---|---|
| FastAPI | Framework web / API REST |
| MySQL | Base de datos (`bdrestaurante`) |
| PyJWT | Generación y validación de tokens JWT |
| bcrypt | Hashing de contraseñas |
| Pydantic | Validación de datos de entrada |

### Estructura

```
AppRestaurante/
├── AppMain.py              # Punto de entrada (FastAPI + CORS)
├── controladores/          # Routers / Endpoints
├── servicios/              # Lógica de negocio
├── dao/                    # Acceso a datos (MySQL)
├── modelos/                # Entidades y DTOs
├── seguridad/              # JWT (generación y validación)
└── resources/              # Configuración (DB, SECRET_KEY)
```

### Endpoints

| Método | Ruta | Descripción |
|---|---|---|
| `POST` | `/api/usuarios/login` | Autenticación con email y password |
| `POST` | `/api/usuarios/registrar` | Registro con password hasheado (bcrypt) |
| `GET` | `/api/usuarios/` | Listar todos los usuarios |

### Ejecución

```bash
cd AppRestaurante
pip install fastapi uvicorn mysql-connector-python pyjwt bcrypt pydantic[email]
uvicorn AppMain:app --reload --port 8000
```

## Frontend — `sistemarestaurante/`

| Tecnología | Uso |
|---|---|
| React 19 | UI / Componentes |
| TypeScript | Tipado estático |
| Vite 8 | Bundler y servidor de desarrollo |
| React Router 7 | Navegación SPA |

### Estructura

```
sistemarestaurante/src/
├── componentes/    # Elementos reutilizables (LoginForm)
├── context/        # AuthProvider (estado global de sesión)
├── dominios/       # DTOs (CUsuarioDTO)
├── hooks/          # Lógica personalizada (useLogin)
├── paginas/        # Vistas (LoginPage, Dashboard)
└── servicios/      # Llamadas a la API del backend
```

### Ejecución

```bash
cd sistemarestaurante
npm install
npm run dev
```

El frontend se levanta en `http://localhost:5173` y se comunica con el backend en `http://localhost:8000`.

## Propuesta mejorada (Actividad 2)

La validación de credenciales se realiza **en el backend (Python)** y no en la base de datos:

1. El DAO busca al usuario solo por email (`SELECT ... WHERE cemail = ?`).
2. El servicio compara el password con **bcrypt** en Python.
3. Las contraseñas se almacenan como hashes bcrypt, nunca en texto plano.
4. La `SECRET_KEY` y las credenciales de BD se leen desde **variables de entorno**.

Esto mejora la separación de responsabilidades y la seguridad frente al enfoque anterior que delegaba la validación a un stored procedure.
