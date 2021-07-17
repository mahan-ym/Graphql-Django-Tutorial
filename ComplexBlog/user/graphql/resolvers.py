from user.models import CustomUser

def resolve_get_users(info, **kwargs):
    return CustomUser.objects.all()

def resolve_get_user(info, **kwargs):
    id = kwargs.get('id')
    if id is not None:
        return CustomUser.objects.get(pk = id)
    else:
        return None