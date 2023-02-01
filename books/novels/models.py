from django.db import models

# Create your models here.
class Novels(models.Model):
    nName = models.CharField(max_length=50)
    nAuthor = models.CharField(max_length=50)
 
    def __str__(self):
        return self.nName