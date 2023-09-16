from django.db import models
class store(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    mobile=models.BigIntegerField()
    password=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
