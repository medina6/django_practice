from django.db import models

class Post(models.Model):
    decription = models.CharField(max_length=55)
    topic = models.CharField(max_length=60)

