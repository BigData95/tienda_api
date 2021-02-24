""" Auxiliar funtionts that both services use """

from app.main import db


def save_changes(data) -> None:
    db.session.add(data)
    db.session.commit()

def success(data):
    response_info = {
        'status': 'Success',
        'message': 'Resource successfully added.'
    }
    # response_object = {**response_info, **data.as_dict()}       # Python>= 3.5 
    response_object = response_info.copy()
    response_object.update(data.as_dict())

    
    return response_object, 201