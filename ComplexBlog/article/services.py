from user.models import CustomUser
from category.models import Category
from django.core.exceptions import ObjectDoesNotExist


def get_author(author_id, field_name='author'):
    try:
        author = CustomUser.objects.get(id=author_id)
        return author
    except ObjectDoesNotExist:
        pass    #handle exceptions

def get_category(category_id, field_name='category'):
    try:
        category = Category.objects.get(id=category_id)
        return category
    except ObjectDoesNotExist:
        pass  