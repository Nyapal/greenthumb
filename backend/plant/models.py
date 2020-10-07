from django.db import models

# Create your models here.
class Plant(models.Model):
  title = models.CharField(max_length=120)
  description = models.TextField()

  def _str(self):
    return self.title