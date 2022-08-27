def ufoEntity(item)-> dict:
    return {
        "id":str(item['_id']),
        "date_time": str(item['date_time']),
        "city":str(item['city']),
        "state":str(item['state']),
        "country":str(item['country']),
        "shape":str(item['shape']),
        "duration": str(item['duration']),
        "summary": str(item['summary']),
        "posted":str(item['posted']),
        "images": str(item['images']),
        "hoax": item['hoax']
    }

def ufosEntity(entity)->list:
    return [ufoEntity(item) for item in entity]