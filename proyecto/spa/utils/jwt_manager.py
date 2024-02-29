import os
from dotenv import load_dotenv
from jwt import encode, decode

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

def create_token (data: dict, secret: str = SECRET_KEY):
	encoded_jwt = encode(data, secret, algorithm="HS256")
	return encoded_jwt

def validate_token(token: str):
	try:
		return decode(token, SECRET_KEY, algorithms=["HS256"])
	except:
		raise Exception("Token is invalid")