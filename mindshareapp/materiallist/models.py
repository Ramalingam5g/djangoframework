from django.db import models
import uuid
Trans_type=(
    ('RF','Recieved from'),
    ("IT","Issued to"),
)
material_choice=(
    ("key board","key board"),
    ("mouse","mouse"),
    ("phone","phone"),
    ("labtop","laptop",)

)
class Material(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    transaction_type=models.CharField(max_length=20,choices=Trans_type,default='RF')
    material_name=models.CharField(max_length=100,choices=material_choice,default='phone')
    date=models.DateField()
    doc_no=models.IntegerField(unique=True)
    received_from=models.CharField(max_length=200,null=True,blank=True)
    issue=models.CharField(max_length=200,null=True,blank=True)
    balance=models.IntegerField()
    verification_date=models.DateField()
    verified_by=models.CharField(max_length=100)
    

# Create your models here.
