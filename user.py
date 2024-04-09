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