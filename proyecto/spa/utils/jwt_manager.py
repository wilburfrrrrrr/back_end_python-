import os
from dotenv import load_dotenv
from jwt import encode, decode
from datetime import datetime, timedelta

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
TOKEN_EXPIRATION = 30

def create_token (data: dict, secret: str = SECRET_KEY):
	data.update({"exp": datetime.utcnow() + timedelta(minutes=TOKEN_EXPIRATION)})
	encoded_jwt = encode(data, secret, algorithm="HS256")
	return encoded_jwt

def validate_token(token: str):
	try:
		return decode(token, SECRET_KEY, algorithms=["HS256"])
	except Exception as e:
		raise e