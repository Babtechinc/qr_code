# Generated by Django 3.1.3 on 2020-11-24 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/Qr_code'),
        ),
    ]
