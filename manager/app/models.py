from django.db import models

class App(models.Model):
    message = models.CharField(max_length=500, blank=True)