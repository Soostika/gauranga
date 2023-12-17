from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self) :
        return f"{self.name} =>{self.address}"
    
