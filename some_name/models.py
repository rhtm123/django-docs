from django.db import models

# Create your models here.

class Blog(models.Model):
	header = models.CharField(max_length=250)
	content = models.TextField()
	author = models.CharField(max_length=100)
	likes = models.IntegerField(default=0)
	dislikes = models.IntegerField(default=0)
	pub_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.header