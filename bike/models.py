from django.db import models
from django.urls import reverse


# Create your models here.
class TwoWheeler(models.Model):
    Model_name = models.CharField(max_length=200)
    Company_name = models.CharField(max_length=100)
    Model_Info = models.CharField(max_length=1000)
    Price_before = models.IntegerField(default=0)
    Price_after = models.IntegerField(default=0)
    Model_img = models.FileField()

    def get_absolute_url(self):
        return reverse('bike:details', kwargs={'pk': self.pk})

    def __str__(self):
        return self.Model_name + '  -  ' + self.Company_name


