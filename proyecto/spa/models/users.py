from config.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from models.memberships import Membership
from sqlalchemy.orm import validates
from validate_email import validate_email

class User(Base):
	__tablename__ = 'users'

	id = Column(Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
	name = Column(String, nullable=False)
	last_name = Column(String, nullable=False)
	email = Column(String, unique=True, nullable=False)
	password = Column(String, nullable=False)
	memberships = Column(Integer, ForeignKey(Membership.id), nullable=False)

	@validates('id')
	def validate_id(self, key, id):
		if id < 0:
			raise AssertionError('Invalid id')
		return id
	
	@validates('memberships')
	def validate_membership(self, key, memberships):
		if memberships < 0:
			raise AssertionError('Invalid membership')
		return memberships

	@validates('email')
	def validate_email(self, key, email):
		if not validate_email(email):
			raise AssertionError('Invalid email')
		return email

	def __repr__(self):
		return f'<User {self.username}>'