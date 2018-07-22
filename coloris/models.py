from django.db import models

# Create your models here.
class Note(models.Model):
    text_field = models.TextField()
    uniq_count = models.IntegerField(default=0)

    def __str__(self):
        return self.text_field
