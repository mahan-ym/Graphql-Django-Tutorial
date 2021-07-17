from article.models import Article

def resolve_get_articles(info, **kwargs):
    return Article.objects.all()

def resolve_get_article(info, **kwargs):
    id = kwargs.get('id')
    if id is not None:
        return Article.objects.get(pk = id)
    else:
        return None