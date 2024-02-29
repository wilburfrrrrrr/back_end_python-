from config.database import Base
from sqlalchemy.orm import relationship, validates
from sqlalchemy import Column, Integer, String, ForeignKey

class Services(Base):
	__tablename__ = 'services'

	id = Column(Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
	service_name = Column(String(10), nullable = False)
	service_description = Column(String(50), nullable=False)
	service_price = Column(Integer, nullable=False)
	membership_id = Column(Integer, ForeignKey('memberships.id'))


	@validates('id')
	def validate_id(self, key, id):
		if id < 0:
			raise AssertionError('Invalid id')
		return id
	
	@validates('membership_id')
	def validate_membership(self, key, membership_id):
		if membership_id < 0:
			raise AssertionError('Invalid membership')
		return membership_id


	def __repr__(self):
		return f'<Services {self.service_name}>'
  