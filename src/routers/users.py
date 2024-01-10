from fastapi import APIRouter, Request, Body, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List

from ..models.users import User, UserUpdate

router = APIRouter()

@router.post("/", response_description="Add new user", status_code = status.HTTP_201_CREATED, response_model=User)
async def create_user(request: Request, cuser: User = Body(...)):
    user = jsonable_encoder(cuser)
    
    existing_user = request.app.mongodb["users"].find_one({"email": user["email"]})
    if existing_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User with this email already exists")

    new_user = request.app.mongodb["users"].insert_one(user)
    created_user = request.app.mongodb["users"].find_one({"_id": new_user.inserted_id})

    return created_user 

@router.get("/", response_description="List all users", response_model=List[User])
async def list_users(request: Request):
    users = list(request.app.mongodb["users"].find()) 
    return users

@router.put("/{id}", response_description="Update a user", response_model=User)
async def update_user(request: Request, id: str, cuser: UserUpdate = Body(...)):
    user = {k: v for k, v in cuser.dict().items() if v is not None}

    if len(user) >= 1:
        update_result = request.app.mongodb["users"].update_one({"_id": id}, {"$set": user})

        if update_result.modified_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found")

    if ( existing_user := request.app.mongodb["users"].find_one({"_id": id})) is not None:
        return existing_user

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found")

@router.delete("/{id}", response_description="Delete a user")
def delete_user(request: Request, id: str, response: Response):
    delete_result = request.app.mongodb["users"].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response 
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found")
        
