from django.db import models

# Create your models here.
class UserData(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    company_name=models.CharField(max_length=50)
    age=models.IntegerField()
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    zip=models.IntegerField()
    email=models.EmailField()
    web=models.CharField(max_length=100)

    def __str__(self):
        return self.first_name