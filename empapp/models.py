from django.db import models

# Create your models here.
class empdet(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(null = True,blank =True,upload_to ="images/")
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    class Meta:
        db_table = "empdt"