from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from src.api import main_router
from src.database import engine
from src.models.base import Base

from src.models.user import User
from src.models.airlane import Airlane
from src.models.flight import Flight
from src.models.flight_status import FlightStatus
from src.models.flight_type import FlightType
from src.models.reservation import Reservation
from src.models.review import Review
from src.models.seat import Seat
from src.models.ticket import Ticket

from starlette_admin.contrib.sqla import Admin, ModelView
from starlette_admin.auth import AdminUser, AuthProvider

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from sqlalchemy.orm import registry

templates = Jinja2Templates(directory="src/templates")

app = FastAPI()

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "message": "Hello from FastAPI"})


@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


app.include_router(main_router)

admin = Admin(engine, title="My Admin")

mapper_registry: registry = Base.registry

for mapper in mapper_registry.mappers:
    model = mapper.class_
    admin.add_view(ModelView(model))

admin.mount_to(app)
