from django.db import models


class material(models.Model):
    date=models.DateField()
    doc_no=models.IntegerField()
    received_from=models.CharField(max_length=200,null=True,blank=True)
    receipt_no=models.IntegerField()
    issue=models.CharField(max_length=200,null=True,blank=True)
    balance=models.IntegerField()
    verification_date=models.DateField()
    verified_by=models.CharField(max_length=100)

    def __str__(self):
        return self.date


# Create your models here.
