#encoding=utf-8
from django.db import models
from django.utils import timezone
import datetime
from mdeditor.fields import MDTextField

# Create your models here.
# 系统用户表
class AccountInformation(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.username
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


# 文章信息表
class Article(models.Model):
    title = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    tags = models.CharField(max_length=30)
    introduction = models.CharField(max_length=180)
    images = models.CharField(max_length=360)
    pub_date = models.DateTimeField('date published')
    content = MDTextField()
    def __str__(self):
        return self.title
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'