# QuickPay Backend - API de Pagos Fintech

Backend para la plataforma de pagos QuickPay, construido con arquitectura de Monolito Modular + Arquitectura Orientada a Eventos (EDA).

---

## Tecnologias que usa el proyecto

| Tecnologia | Proposito |
|------------|-----------|
| FastAPI | Framework web asincrono para la API REST |
| Uvicorn | Servidor ASGI para ejecutar FastAPI |
| PostgreSQL | Base de datos relacional principal |
| Redis | Cache y manejo de sesiones JWT |
| RabbitMQ | Broker de mensajes para comunicacion asincrona (EDA) |
| SQLAlchemy | ORM para base de datos |
| Alembic | Migraciones de base de datos |
| python-jose | Manejo de tokens JWT |
| bcrypt | Hashing de contrasenas |
| cryptography | Cifrado AES-256 para datos sensibles |
| pytest | Pruebas unitarias e integracion |
| Docker | Contenerizacion del proyecto |
| Docker Compose | Orquestacion de contenedores |

---

## Organizacion de la carpeta

QUICKPACK_BACK_END/
│
├── app/
│ ├── main.py # Punto de entrada de la app
│ ├── api/ # Endpoints REST (v1/auth, payments, users)
│ ├── modules/ # Modulos de negocio (auth, payments, banking)
│ ├── events/ # Comunicacion EDA (broker, publishers, subscribers)
│ ├── core/ # Configuracion central (DB, Redis, security)
│ ├── middleware/ # Middlewares (JWT, rate limiter)
│ └── utils/ # Utilidades (validators, helpers)
│
├── infrastructure/
│ ├── docker/ # Dockerfile y configuracion de contenedores
│ └── scripts/ # Scripts de utilidad (seed_db.py)
│
├── tests/ # Pruebas unitarias y de integracion
├── requirements.txt # Dependencias del proyecto
├── docker-compose.yml # Orquestacion de servicios
├── .env # Variables de entorno
└── README.md


---

## Como ejecutar el proyecto

### Requisitos previos

- Tener Docker y Docker Compose instalados
- Tener Git instalado

### Pasos para ejecutar

1. Clonar el repositorio

```bash
git clone https://github.com/tu-org/QUICKPACK_BACK.git
cd QUICKPACK_BACK

2. Crear archivo de variables de entorno

cp .env.example .env

3. Construir y levantar los contenedores

docker-compose up --build