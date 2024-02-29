from fastapi import APIRouter, Path, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from config.database import Session
from middlewares.jwt_bearer import JWTBearer
from services.agenda import AgendaService
from services.users import UserService
from services.services import ServicesService
from schemas.agenda import Agenda as AgendaSchema

agenda_router = APIRouter()

def validate_memberships(user_id, service_id):
	user = UserService(Session()).get_user(user_id)
	service = ServicesService(Session()).get_service_by_id(service_id)
	if not user or not service:
		raise ValueError("User or service not found")
	if user.memberships < service.membership_id:
		raise ValueError("User cannot access this service")		

@agenda_router.post("/", response_description="Agenda data added into the database")
async def add_agenda_data(agenda: AgendaSchema, token: str = Depends(JWTBearer())):
	user_id = token.get("id")
	validate_memberships(user_id, agenda.service_id)
	agenda_json = jsonable_encoder(agenda)
	agenda_json["user_id"] = user_id
	if not agenda_json:
		return JSONResponse(status_code=400, content={"message": "Invalid data"})
	AgendaService(Session()).create_agenda(agenda_json)
	return JSONResponse(status_code=200, content={"message": "Agenda data added successfully"})

@agenda_router.get("/", response_description="Agenda data retrieved")
async def get_agenda_data(token: str = Depends(JWTBearer())):
	agenda = AgendaService(Session()).get_all_agendas()
	if not agenda:
		return JSONResponse(status_code=404, content={"message": "No agenda data available"})
	return agenda

@agenda_router.put("/{id}")
async def update_agenda_data(agenda: AgendaSchema, id: int = Path(..., title="The ID of the agenda to update"),  token: str = Depends(JWTBearer())):
	if not AgendaService(Session()).get_agenda_by_id(id):
		return JSONResponse(status_code=400, content={"message": "Invalid data"})
	AgendaService(Session()).update_agenda(id, agenda)
	return JSONResponse(status_code=200, content={"message": "Agenda data updated successfully"})

@agenda_router.delete("/{id}", response_description="Agenda data deleted from the database")
async def delete_agenda_data(id: int = Path(..., title="The ID of the agenda to delete"), token: str = Depends(JWTBearer())):
	AgendaService(Session()).delete_agenda(id)
	return JSONResponse(status_code=200, content={"message": "Agenda data deleted successfully"})

@agenda_router.get("/user/{id}", response_description="Agenda data retrieved")
async def get_agenda_data_by_user_id(id: int = Path(..., title="The ID of the user to retrieve"), token: str = Depends(JWTBearer())):
	agenda = AgendaService(Session()).get_agenda_by_user_id(id)
	if agenda:
		return agenda
	return JSONResponse(status_code=404, content={"message": "Agenda not found"})

@agenda_router.get("/user", response_description="Agenda data retrieved")
async def get_agenda_data_by_user(token: str = Depends(JWTBearer())):
	user_id = token.get("id")
	agenda = AgendaService(Session()).get_agenda_by_user_id(user_id)
	if agenda:
		return agenda
	return JSONResponse(status_code=404, content={"message": "Agenda not found"})

@agenda_router.get("/{id}", response_description="Agenda data retrieved")
async def get_agenda_data_by_id(id: int = Path(..., title="The ID of the agenda to retrieve"), token: str = Depends(JWTBearer())):
	agenda = AgendaService(Session()).get_agenda_by_id(id)
	if agenda:
		return agenda
	return JSONResponse(status_code=404, content={"message": "Agenda not found"})

@agenda_router.put("/done/{id}")
async def mark_as_done(id: int = Path(..., title="The ID of the agenda to mark as done"), token: str = Depends(JWTBearer())):
	AgendaService(Session()).mark_as_done(id)
	return JSONResponse(status_code=200, content={"message": "Agenda marked as done successfully"})


