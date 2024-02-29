from pydantic import BaseModel, Field

class Membership(BaseModel):
	membership_level: str = Field(..., alias='membership_level')

	class Config:
		orm_mode = True
		model_config = {
			"json_schema_extra": {
				"example": {
					"membership_level": "Esencial"
				}
			}
		}
