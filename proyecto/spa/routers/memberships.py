from fastapi import APIRouter
from models.memberships import Membership 
from schemas.memberships import Membership as MembershipSchema
from services.memberships import MembershipService
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from config.database import Session

memberships_router = APIRouter()

@memberships_router.post("/", response_description="Membership data added into the database")
async def add_membership_data(membership: MembershipSchema):
	membership = jsonable_encoder(membership)
	if not membership:
		return JSONResponse(status_code=400, content={"message": "Invalid data"})
	MembershipService(Session()).create_membership(membership)
	return JSONResponse(status_code=200, content={"message": "Membership data added successfully"})

@memberships_router.get("/", response_description="Membership data retrieved")
async def get_membership_data():
	membership = MembershipService(Session()).get_all_memberships()
	if not membership:
		return JSONResponse(status_code=404, content={"message": "No membership data available"})
	return membership

@memberships_router.put("/{id}")
async def update_membership_data(membership: MembershipSchema, id: int):
	if not MembershipService(Session()).get_membership_by_id(id):
		return JSONResponse(status_code=400, content={"message": "Invalid data"})
	MembershipService(Session()).update_membership(id, membership)
	return JSONResponse(status_code=200, content={"message": "Membership data updated successfully"})

@memberships_router.delete("/{id}", response_description="Membership data deleted from the database")
async def delete_membership_data(id: int):
	MembershipService(Session()).delete_membership(id)
	return JSONResponse(status_code=200, content={"message": "Membership data deleted successfully"})

@memberships_router.get("/{id}", response_description="Membership data retrieved")
async def get_membership_data_by_id(id: int):
	membership = MembershipService(Session()).get_membership_by_id(id)
	if membership:
		return membership
	return JSONResponse(status_code=404, content={"message": "Membership not found"})



