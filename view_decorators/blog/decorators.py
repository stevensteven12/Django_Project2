from django.core.exceptions import PermissionDenied
from .models import Article


def user_is_article_author(function):
    def wrap(request, *args, **kwargs):
        article = Article.objects.get(id=kwargs['article_id'])
        if article.create_by == request.user:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap