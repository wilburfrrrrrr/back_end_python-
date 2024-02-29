from typing import Optional
from pydantic import BaseModel, Field

class Agenda(BaseModel):
	title: str = Field(default='Agenda', alias='title', min_length=4, max_length=100)
	date: str = Field(alias='date')
	is_done: bool = Field(default=False, alias='is_done')
	user_id: int = Field(..., alias='user_id')
	service_id: int = Field(..., alias='service_id')

	class Config:
		orm_mode = True
		model_config = {
			"json_schema_extra": {
				"example": {
					"title": "Agenda",
					"date": "2021-01-01",
					"is_done": False,
					"user_id": 1,
					"service_id": 1
				}
			}
		}

