from models.agenda import Agenda
from schemas.agenda import Agenda as AgendaSchema
from datetime import datetime

class AgendaService():
	def __init__(self, db):
		self.db = db

	def create_agenda(self, agenda: AgendaSchema):
		agenda["date"] = datetime.strptime(agenda["date"], "%Y-%m-%dT%H:%M:%S")
		new_agenda = Agenda(**agenda)
		self.db.add(new_agenda)
		self.db.commit()

	def get_all_agendas(self):
		return self.db.query(Agenda).all()
	
	def get_agenda_by_id(self, id: int):
		return self.db.query(Agenda).filter(Agenda.id == id).first()
	
	def get_agenda_by_user_id(self, user_id: int):
		return self.db.query(Agenda).filter(Agenda.user_id == user_id).first()
	
	def update_agenda(self, id: int, agenda: AgendaSchema):
		current_agenda = self.get_agenda_by_id(id)
		current_agenda.title = agenda.title
		current_agenda.description = agenda.description
		current_agenda.date = agenda.date
		current_agenda.time = agenda.time
		current_agenda.user_id = agenda.user_id 
		self.db.commit()

	def delete_agenda(self, id: int):
		self.db.query(Agenda).filter(Agenda.id == id).delete()
		self.db.commit()

	def mark_as_done(self, id: int):
		current_agenda = self.get_agenda_by_id(id)
		current_agenda.is_done = True
		self.db.commit()