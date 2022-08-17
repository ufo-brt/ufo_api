def ufoEntity(item)-> dict:
    return{
        "id":item['id'],
        "name":item['name'],
        "email":item['email'],
        "password":item['password']
    }

def ufosEntity(entity)->list:
    return [ufoEntity(item) for item in entity]