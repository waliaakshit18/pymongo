#here document format is lil bit diff than mongo
#we need to conver in json first

#object id to string
from fastapi import APIRouter

from model.user import User
from config.db import conn
from schemas.user import usersEntity
from schemas.user import userEntity
from bson import ObjectId
user = APIRouter()

@user.get('/')
async def find_all_user():
    print(conn.local.user.find())
    print(usersEntity(conn.local.user.find()) )
    return usersEntity(conn.local.user.find())


@user.post('/')
async def create_user(user:User):
    conn.local.user.insert_one(dict(user))
    return usersEntity(conn.local.user.find())

@user.get('/{id}')
async def find_one_user(id):
    return userEntity(conn.local.user.find_one({"_id":ObjectId(id)}) )



@user.patch('/{id}')
async def update_user(id,user:User):
     conn.local.user.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(user)
    })  #mongo db undesrtand inly ibject id so convert it
     return usersEntity(conn.local.user.find_one({"_id":ObjectId(id)}))



@user.delete('/{id}')
async def delete_user(id,user:User):
     return userEntity(conn.local.user.find_one_and_delete({"_id":ObjectId(id)}) )  #mongo db undesrtand inly ibject id so convert it



def userEntity(item) -> dict:
    return {
        "id":str(item["_id"]),
        "name":item["name"],
        "age":item["age"],
        "address":item["address"]
    }

#user entity of single document,but in find all methods we get array of object
def usersEntity(entity)->list:

    return [userEntity(item) for item in entity]

#here document format is lil bit diff than mongo
#we need to conver in json first

#object id to string

def userEntity(item) -> dict:
    return {
        "id":str(item["_id"]),
        "name":item["name"],
        "age":item["age"],
        "address":item["address"]
    }

#user entity of single document,but in find all methods we get array of object
def usersEntity(entity)->list:

    return [userEntity(item) for item in entity]

