from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import requests, FastAPI, Response
from fastapi.responses import JSONResponse

class ErrorHandler(BaseHTTPMiddleware):
	def __init__(self, app: FastAPI):
		super().__init__(app)

	async def dispatch(self, request: requests.Request, call_next):
		try:
			return await call_next(request)
		except Exception as e:
			print(e)
			return JSONResponse(status_code=500, content={"message": "Server Error"})
