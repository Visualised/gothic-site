class APIError(Exception):
    pass


class ObjectDoesNotExist(APIError):
    description = "Object does not exist."
    code = 404


class WrongType(APIError):
    description = "Your object has wrong 'type' data"
    code = 400


class WrongGuild(APIError):
    description = "Your object has wrong 'guild' data"
    code = 400
