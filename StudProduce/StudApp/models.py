from django.db import models
'''
GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other')
)
'''
# Create your models here.
class StudDB(models.Model):
    First_Name = models.CharField(max_length=15)
    Last_Name = models.CharField(max_length=15)
    Email=models.EmailField(default='xyz@gmail.com')
    Age  = models.IntegerField(default=20)
    Mobile=models.BigIntegerField()
    Gender= models.CharField(max_length=10)
    Remarks=models.CharField(max_length=50)
    #Country=models.CharField(max_length=10)
    #Skils=models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    isActive=models.BooleanField()

    def __str__(self):
        return self.Name

