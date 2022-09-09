# Generated by Django 3.2.6 on 2022-09-09 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_userinfo_third_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='city',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='country',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='province',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='avatar_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
