from config.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import validates

class Membership(Base):
	__tablename__ = 'memberships'

	id = Column(Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
	membership_level = Column(String)

	@validates('id')
	def validate_id(self, key, id):
		if id < 0:
			raise AssertionError('Invalid id')
		return id
	
	def __repr__(self):
		return f'<Membership {self.membership_level}>'