class APIError(Exception):
    pass

class ObjectDoesNotExist(APIError):
    description = "Object does not exist."
    code = 404

class WrongType(APIError):
    description = "Your object has wrong type data"
    code = 400