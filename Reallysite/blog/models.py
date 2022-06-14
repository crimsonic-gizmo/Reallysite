from django.db import models

# Create your models here.

#class テーブル名(models.Moldel):
#	カラム名 = models.型名() 
class Article(models.Model):
	title = models.CharField(default="", max_length=30)
	text = models.TextField(default="",)
	author = models.CharField(default="", max_length=30)
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)


