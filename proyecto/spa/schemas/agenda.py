from typing import Optional
from pydantic import BaseModel, Field

class Agenda(BaseModel):
	date: str = Field(alias='date')
	is_done: bool = Field(default=False, alias='is_done')
	# user_id: int = Field(..., alias='user_id')
	service_id: int = Field(..., alias='service_id')

	class Config:
		orm_mode = True
		model_config = {
			"json_schema_extra": {
				"example": {
					"date": "2024-02-28T15:30:00",
					"is_done": False,
					# "user_id": 1,
					"service_id": 1
				}
			}
		}

