from typing import Optional
from pydantic import BaseModel, Field

class Service(BaseModel):
	service_name: str = Field(..., alias='service_name')
	service_description: str = Field(..., alias='service_description')
	service_price: int = Field(..., alias='service_price')
	membership_id: int = Field(None, alias='membership_id')

	class Config:
		orm_mode = True
		model_config = {
			"json_schema_extra": {
				"example": {
					"service_name": "Service",
					"service_description": "Service description",
					"service_price": 100,
					"membership_id": 1
				}
			}
		}