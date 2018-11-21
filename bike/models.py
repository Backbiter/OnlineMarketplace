from django.db import models


# Create your models here.
class TwoWheeler(models.Model):
    Model_name = models.CharField(max_length=200)
    Company_name = models.CharField(max_length=100)

    def __str__(self):
        return self.Model_name + '  -  ' + self.Company_name
