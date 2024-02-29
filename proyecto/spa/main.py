from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from config.database import engine, Base
from middlewares.error import ErrorHandler
from routers.agenda import agenda_router
from routers.users import user_router
from routers.auth import auth_router
from routers.services import service_router
from routers.memberships import memberships_router

app = FastAPI()
app.title = "SPA"
app.version = "2.0"

app.add_middleware(ErrorHandler)
app.include_router(auth_router)
app.include_router(agenda_router, tags=["Agenda"], prefix="/agenda")
app.include_router(user_router, tags=["Users"], prefix="/users")
app.include_router(memberships_router, tags=["Memberships"], prefix="/memberships")
app.include_router(service_router, tags=["Services"], prefix="/services")

Base.metadata.create_all(bind=engine)

@app.get("/", tags=["home"], response_class=HTMLResponse)
async def read_root():
	return HTMLResponse(content="<h1>SPA API</h1>", status_code=200)