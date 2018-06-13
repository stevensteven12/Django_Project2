from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name='标题')
    create_by = models.ForeignKey(User, verbose_name='用户', on_delete=models.CASCADE,)
    create_date = models.DateTimeField(auto_created=True, verbose_name='创建时间')

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

