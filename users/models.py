from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=1000)
    document = models.FileField(upload_to='documents/', default='default.txt')

    def _str_(self):
        return self.title
