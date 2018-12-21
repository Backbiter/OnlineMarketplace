from django.db import models

Cities = (('p','Pune'), ('b','Bangalore'), ('m','Mumbai'), )


# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=50, choices=Cities)

    def __str__(self):
        return self.name + '  ' + self.city

