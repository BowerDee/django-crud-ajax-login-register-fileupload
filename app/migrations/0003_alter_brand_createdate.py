# Generated by Django 3.2.6 on 2022-09-13 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_last_step_id_roleinfo_last_step'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='createdate',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]