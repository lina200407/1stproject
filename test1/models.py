from django.db import models

# Create your models here.
class Project(models.Model):
    projectname = models.CharField(max_length=50)
    description = models.TextField()
    pr_photo = models.ImageField(upload_to='photos',null=True,blank=True)
    
    def __str__(self):
        return self.projectname
    
class About(models.Model):
    text = models.TextField()

class ContactInfo(models.Model):
    instagram = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
   


