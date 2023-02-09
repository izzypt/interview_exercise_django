from django.db import models

# Create your models here.
class ScanModel(models.Model):
    id = models.AutoField(primary_key=True)
    value = models.CharField(max_length=100)
    
    def __str__(self):
        return self.value

class FindingsModel(models.Model):
    id = models.AutoField(primary_key=True)
    target_id = models.CharField(max_length=100)
    definition_id = models.CharField(max_length=100)
    scans = models.ManyToManyField(ScanModel)
    url = models.CharField(max_length=200)
    path = models.CharField(max_length=200)
    method = models.CharField(max_length=10)
    
    def __str__(self):
        return str(self.id)