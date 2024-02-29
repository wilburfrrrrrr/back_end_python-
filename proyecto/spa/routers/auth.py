from fastapi import APIRouter
from utils.jwt_manager import create_token
from fastapi.responses import JSONResponse
from schemas.auth import Auth 
from services.users import UserService
from config.database import Session


auth_router = APIRouter()

@auth_router.post('/login')
async def login(user: Auth):
	current_user = await UserService(Session()).authenticate_user(user)
	if not current_user:
		return JSONResponse(status_code=401, content={"message": "Invalid Credentials"})
	token_dict = {
		"id": current_user.id,
		"name": current_user.name,
		"last_name": current_user.last_name,
		"email": current_user.email,
		"membership": current_user.memberships,
	}
	token = create_token(token_dict)
	return JSONResponse(status_code=200, content={"token": token, "token_type": "bearer"})


