from fastapi import APIRouter
from utils.jwt_manager import create_token
from fastapi.responses import JSONResponse
from schemas.users import User 
from services.users import UserService
from config.database import Session


auth_router = APIRouter()

@auth_router.post('/login')
async def login(user: User):
	current_user = await UserService(Session()).authenticate_user(user.email, user.password)
	if not current_user:
		return JSONResponse(status_code=401, content={"message": "Invalid Credentials"})
	token = create_token(current_user)
	return JSONResponse(status_code=200, content={"token": token, "token_type": "bearer"})


