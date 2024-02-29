from models.memberships import Membership
from schemas.memberships import Membership as MembershipSchema


class MembershipService():
	def __init__(self, db):
		self.db = db

	def create_membership(self, membership: MembershipSchema):
		new_membership = Membership(**membership)
		self.db.add(new_membership)
		self.db.commit()

	def get_all_memberships(self):
		return self.db.query(Membership).all()
	
	def get_membership_by_id(self, id: int):
		return self.db.query(Membership).filter(Membership.id == id).first()
	
	def update_membership(self, id: int, membership: MembershipSchema):
		current_membership = self.get_membership_by_id(id)
		current_membership.membership_level = membership.membership_level
		self.db.commit()

	def delete_membership(self, id: int):
		self.db.query(Membership).filter(Membership.id == id).delete()
		self.db.commit()