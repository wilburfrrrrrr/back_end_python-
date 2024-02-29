from pydantic import BaseModel, Field

class User(BaseModel):
	name: str = Field(..., alias='name', min_length=4, max_length=100)
	last_name: str = Field(..., alias='last_name', min_length=4, max_length=100)
	email: str = Field(..., alias='email')
	password: str = Field(..., min_length=8, max_length=20, alias='password')
	memberships: int = Field(..., alias='memberships')

	class Config:
		orm_mode = True
		model_config = {
			"json_schema_extra": {
				"example": {
					"username": "User",
					"email": "",
					"user_id": 1,
					"service_id": 1
				}
			}
		}