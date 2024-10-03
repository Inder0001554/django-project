from django.db import models

# makemigrate - create changes and store in a file
# migrate - apply the pending changes create by makemigrations

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=122)
    desc = models.TextField()
    date = models.DateField()
    
# show name in backend    <<-- add manually    
def  __str__(self):
    return self.name    
