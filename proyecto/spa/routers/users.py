from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from services.users import UserService
from schemas.users import User as UserSchema
from config.database import Session


user_router = APIRouter()

@user_router.post("/", response_description="User data added into the database")
async def add_user_data(user: UserSchema):
	user = jsonable_encoder(user)
	if not user:
		return JSONResponse(status_code=400, content={"message": "Invalid data"})
	UserService(Session()).create_user(user)
	return JSONResponse(status_code=200, content={"message": "User data added successfully"})

@user_router.get("/", response_description="User data retrieved")
async def get_user_data():
	user = UserService(Session()).get_users()
	if not user:
		return JSONResponse(status_code=404, content={"message": "No user data available"})
	# return JSONResponse(status_code=200, content=user)
	return user

@user_router.put("/{id}")
async def update_user_data(user: UserSchema, id: int):
	if not UserService(Session()).get_user(id):
		return JSONResponse(status_code=400, content={"message": "Invalid data"})
	print("updating	")
	UserService(Session()).update_user(id, user)
	return JSONResponse(status_code=200, content={"message": "User data updated successfully"})

@user_router.delete("/{id}", response_description="User data deleted from the database")
async def delete_user_data(id: int):
	UserService(Session()).delete_user(id)
	return JSONResponse(status_code=200, content={"message": "User data deleted successfully"})

@user_router.get("/{id}", response_description="User data retrieved")
async def get_user_data_by_id(id: int):
	user = UserService(Session()).get_user(id)
	if user:
		# return JSONResponse(status_code=200, content=user)
		return user
	return JSONResponse(status_code=404, content={"message": "User not found"})

@user_router.get("/mail/{mail}", response_description="User data retrieved")
async def get_user_data_by_mail(mail: str):
	user = UserService(Session()).get_user_by_mail(mail)
	if user:
		# return JSONResponse(status_code=200, content=user)
		return user
	return JSONResponse(status_code=404, content={"message": "User not found"})





