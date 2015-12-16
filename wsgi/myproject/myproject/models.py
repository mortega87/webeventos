from django.db import models

class Evento(models.Model):
    name = models.CharField(maxlength=30)
