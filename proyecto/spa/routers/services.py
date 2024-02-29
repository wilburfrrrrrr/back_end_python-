from fastapi import APIRouter, Path, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from services.services import ServicesService
from schemas.services import Service as ServiceSchema
from config.database import Session

service_router = APIRouter()

@service_router.post("/", response_description="Service data added into the database")
async def add_service_data(service: ServiceSchema):
	service = jsonable_encoder(service)
	if not service:
		return JSONResponse(status_code=400, content={"message": "Invalid data"})
	ServicesService(Session()).create_service(service)
	return JSONResponse(status_code=200, content={"message": "Service data added successfully"})

@service_router.get("/", response_description="Service data retrieved")
async def get_service_data():
	service = ServicesService(Session()).get_all_services()
	if not service:
		return JSONResponse(status_code=404, content={"message": "No service data available"})
	return service

@service_router.put("/{id}")
async def update_service_data(service: ServiceSchema, id: int = Path(..., title="The ID of the service to update")):
	if not ServicesService(Session()).get_service_by_id(id):
		return JSONResponse(status_code=400, content={"message": "Invalid data"})
	ServicesService.update_service(id, service)
	return JSONResponse(status_code=200, content={"message": "Service data updated successfully"})

@service_router.delete("/{id}", response_description="Service data deleted from the database")
async def delete_service_data(id: int = Path(..., title="The ID of the service to delete")):
	ServicesService(Session()).delete_service(id)
	return JSONResponse(status_code=200, content={"message": "Service data deleted successfully"})

@service_router.get("/{id}", response_description="Service data retrieved")
async def get_service_data(id: int = Path(..., title="The ID of the service to get")):
	service = ServicesService(Session()).get_service(id)
	if service:
		return service
	return JSONResponse(status_code=404, content={"message": "Service data not found"})






