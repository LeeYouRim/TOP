from django.db import models

# Create your models here.

class todays(models.Model):
    category = models.CharField(max_length=700)
    brand = models.CharField(max_length=200)
    title = models.CharField(max_length=200, primary_key=True)
    today = models.CharField(max_length=200)
    class Meta:
        db_table = "todays"