from django.db import models
import uuid

class material(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date=models.DateField()
    doc_no=models.IntegerField()
    received_from=models.CharField(max_length=200,null=True,blank=True)
    receipt_no=models.IntegerField()
    issue=models.CharField(max_length=200,null=True,blank=True)
    balance=models.IntegerField()
    verification_date=models.DateField()
    verified_by=models.CharField(max_length=100)
    

    

# Create your models here.
