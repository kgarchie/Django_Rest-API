from django.db import models

# Create your models here.


class Members(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    yr_joined = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name

