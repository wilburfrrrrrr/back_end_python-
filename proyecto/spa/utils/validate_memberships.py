from services.services import ServicesService
from services.users import UserService
from config.database import Session

def validate_memberships(user_id, service_id):
	user = UserService(Session()).get_user(user_id)
	service = ServicesService(Session()).get_service_by_id(service_id)
	if not user or not service:
		raise ValueError("User or service not found")
	if user.memberships < service.membership_id:
		raise ValueError("User cannot access this service")		