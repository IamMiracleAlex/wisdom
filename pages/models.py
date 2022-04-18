from django.db import models


class Quote(models.Model):
	author = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True)
	body = models.TextField()
	make_public = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)