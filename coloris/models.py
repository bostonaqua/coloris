from django.db import models

# Create your models here.
class note(models.Model):
    text_field = models.TextField()