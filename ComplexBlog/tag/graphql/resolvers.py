from tag.models import Tag

def resolve_get_tags(info, **kwargs):
    return Tag.objects.all()

def resolve_get_tag(info, **kwargs):
    id = kwargs.get('id')
    if id is not None:
        return Tag.objects.get(pk = id)
    else:
        return None