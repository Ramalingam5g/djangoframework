# Generated by Django 3.2.5 on 2021-07-20 13:25

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('bincardcreation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
