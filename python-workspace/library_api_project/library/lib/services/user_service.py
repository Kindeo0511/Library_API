from library.models import UserModel

def register_user(data):

    return UserModel.objects.create_user(**data)


