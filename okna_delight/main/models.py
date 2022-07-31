from django.db import models


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=15)

