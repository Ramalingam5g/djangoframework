# Generated by Django 3.2.5 on 2021-08-02 11:54

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('doc_no', models.IntegerField()),
                ('received_from', models.CharField(blank=True, max_length=200, null=True)),
                ('receipt_no', models.IntegerField(unique=True)),
                ('issue', models.CharField(blank=True, max_length=200, null=True)),
                ('balance', models.IntegerField()),
                ('verification_date', models.DateField()),
                ('verified_by', models.CharField(max_length=100)),
            ],
        ),
    ]
