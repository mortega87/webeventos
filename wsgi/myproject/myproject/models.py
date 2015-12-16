from django.db import models

class Evento(models.Model):
    name = models.CharField(max_length=30)
