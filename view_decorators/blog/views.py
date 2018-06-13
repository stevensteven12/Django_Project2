from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .models import Article
from .decorators import user_is_article_author


# Create your views here.

@login_required
def index(request):
    # 获取所有的文章列表
    articles = Article.objects.all()
    return render(request, 'index.html', {'articles': articles})


@login_required
@user_is_article_author
def remove(request, article_id):
    # 如果查询不到文章，则直接抛出异常
    article = get_object_or_404(Article, id=article_id)
    # 删除成功之后的提示信息
    message = '文章：{0}，删除成功'.format(article.title)
    # 删除文章
    article.delete()
    # 把message添加到request
    messages.success(request, message)
    # 转到index函数
    return redirect('index')
