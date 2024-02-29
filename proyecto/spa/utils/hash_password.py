from passlib import context

def hash_password(password):
	return context.CryptContext(schemes=["bcrypt"]).hash(password)

def verify_password(password, hashed_password):
	return context.CryptContext(schemes=["bcrypt"]).verify(password, hashed_password)


