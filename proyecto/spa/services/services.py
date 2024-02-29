from models.services import Services
from schemas.services import Service as ServicesSchema

class ServicesService():
	def __init__(self, db):
		self.db = db

	def create_service(self, service: ServicesSchema):
		new_service = Services(**service)
		self.db.add(new_service)
		self.db.commit()

	def get_all_services(self):
		return self.db.query(Services).all()
	
	def get_service_by_id(self, id: int):
		return self.db.query(Services).filter(Services.id == id).first()
	
	def update_service(self, id: int, service: ServicesSchema):
		current_service = self.get_service_by_id(id)
		current_service.service_name = service.service_name
		current_service.service_description = service.service_description
		current_service.service_price = service.service_price
		current_service.membership_id = service.membership_id
		self.db.commit()

	def delete_service(self, id: int):
		self.db.query(Services).filter(Services.id == id).delete()
		self.db.commit()

