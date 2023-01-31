from django.db import models

# Create your models here.
class BoxDetails(models.Model):
    name= models.CharField(max_length=70)
    qbox_no=models.IntegerField(blank=True,null=True)
    email= models.EmailField(blank=True,max_length=70,null=True)
    password= models.CharField(blank=True,max_length=70,null=True)
    source=models.CharField(max_length=70,blank=True)
    teleport=models.CharField(blank=True,max_length=70,null=True)
    sudo_password=models.CharField(blank=True,max_length=70,null=True)
    apihub=models.CharField(blank=True,max_length=70,null=True)
    web_frontend=models.CharField(blank=True,max_length=70,null=True)
    checkpoints=models.CharField(blank=True,max_length=70,null=True)
    dcmio=models.CharField(blank=True,max_length=70,null=True)
    cxr_api=models.CharField(blank=True,max_length=70,null=True)
    additional=models.TextField(blank=True,null=True)
    
