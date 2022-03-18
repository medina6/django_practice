from django.db import models

class Comment(models.Model):
    useful = models.CharField(max_length=20)
    interesting_comments = models.CharField(max_length=30)

