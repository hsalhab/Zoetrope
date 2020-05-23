from django.db import models

class App(models.Model):
    field = models.CharField(max_length=100)
