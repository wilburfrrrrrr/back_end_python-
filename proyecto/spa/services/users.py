from models.users import User
from schemas.users import User as UserSchema
from schemas.auth import Auth as AuthUser
from utils.hash_password import hash_password, verify_password

class UserService():
	def __init__(self, db):
		self.db = db

	def create_user(self, user: UserSchema):
		print(user)
		user["password"] = hash_password(user["password"])
		new_user = User(**user)
		self.db.add(new_user)
		self.db.commit()

	def get_users(self):
		return self.db.query(User).all()

	def get_user(self, id: int):
		return self.db.query(User).filter(User.id == id).first()
	
	def get_user_by_email(self, email: str):
		return self.db.query(User).filter(User.email == email).first()
	
	def update_user(self, id: int, user: UserSchema):
		current_user = self.db.query(User).filter(User.id == id).first()
		current_user.username = user.username
		current_user.email = user.email
		current_user.password = user.password
		current_user.memberships = user.memberships
		self.db.commit()

	def delete_user(self, id: int):
		self.db.query(User).filter(User.id == id).delete()
		self.db.commit()

	async def authenticate_user(self, login: AuthUser):
		user = self.get_user_by_email(login.email)
		if user and verify_password(login.password, user.password):
			return user
		return None