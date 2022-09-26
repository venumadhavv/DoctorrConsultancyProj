from django.db import models

# Create your models here.
import uuid




class Patient(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=50)
    mobile_number=models.CharField(max_length=10)
    age=models.IntegerField(default=1)
    country=models.CharField(max_length=10,default='select')
    state=models.CharField(max_length=10,default='select')
    city=models.CharField(max_length=10,default='select')
    created_at=models.DateTimeField(auto_now_add=True)
    user_id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
        return self.name 

class Doctor(models.Model):
    dname=models.CharField(max_length=50)
    demail=models.EmailField(max_length=50)
    dpassword=models.CharField(max_length=50)
    dmobile_number=models.CharField(max_length=10)
    dage=models.IntegerField(default=1)
    dspecial=models.CharField(max_length=50)
    dexperience=models.IntegerField(default=0)

    dcountry=models.CharField(max_length=10)
    dstate=models.CharField(max_length=10)
    dcity=models.CharField(max_length=10)

    dcreated_at=models.DateTimeField(auto_now_add=True)
    doctor_id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
        return self.dname 