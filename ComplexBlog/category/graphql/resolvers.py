from category.models import Category

def resolve_get_categories(info, **kwargs):
    return Category.objects.all()

def resolve_get_category(info, **kwargs):
    id = kwargs.get('id')
    if id is not None:
        return Category.objects.get(pk = id)
    else:
        return None