# Generated by Django 3.2.6 on 2022-09-13 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_brand_createdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='createdate',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]