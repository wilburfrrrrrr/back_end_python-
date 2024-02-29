from config.database import Base
from sqlalchemy.orm import validates
from models.users import User
from models.services import Services
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from datetime import datetime

class Agenda(Base):
	__tablename__ = 'agendas'

	id = Column(Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
	date = Column(DateTime, nullable = False)
	is_done = Column(Boolean, nullable = False, default=False)
	user_id = Column(Integer, ForeignKey(User.id))
	service_id = Column(Integer, ForeignKey(Services.id))
	# user = relationship('User')
	# service = relationship('Services')

	@validates('service_id')
	def valid_membership(self, key, service_id):
		service = Services.query.get(service_id)
		if not service:
			raise AssertionError('Service does not exist')
		user_membership = User.query.get(self.user_id).memberships
		if 0 <= user_membership < service.membership_id:
			raise AssertionError('User does not have the membership to get this service')
		return service_id
	
	@validates('date')
	def validate_date(self, key, date):
		if date < datetime.now():
			raise AssertionError('Invalid date')
		return date
	
	@validates('user_id')
	def validate_user(self, key, user_id):
		if user_id < 0:
			raise AssertionError('Invalid user')
		return user_id

	def __repr__(self):
		return f'<Agenda {self.title}>'