from django.db import models

class PhoneNumber(models.Model):
    id = models.AutoField(primary_key=True)  # или models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=255)
    default_photo = models.ImageField(upload_to='photos/', null=True, blank=True)
    Phone1 = models.CharField(max_length=20)
    Phone2 = models.CharField(max_length=20, null=True, blank=True)
    Phone3 = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.Name
