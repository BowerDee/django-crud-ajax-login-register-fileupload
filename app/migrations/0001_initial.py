# Generated by Django 3.2.6 on 2022-09-09 03:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=128)),
                ('text', models.CharField(max_length=1024)),
                ('enable', models.BooleanField()),
                ('createdate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('topic', models.CharField(max_length=128)),
                ('describtion', models.CharField(max_length=255)),
                ('tips', models.CharField(max_length=255)),
                ('qtype', models.IntegerField()),
                ('stage', models.IntegerField()),
                ('skip', models.BooleanField()),
                ('score', models.IntegerField()),
                ('op_1', models.CharField(max_length=255)),
                ('op_2', models.CharField(max_length=255)),
                ('op_3', models.CharField(max_length=255)),
                ('op_4', models.CharField(max_length=255)),
                ('correct', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='RoleInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('last_stage', models.IntegerField()),
                ('last_question_id', models.IntegerField()),
                ('updatedate', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('createdate', models.DateTimeField(auto_now_add=True)),
                ('updatedate', models.DateTimeField(auto_now=True)),
                ('username', models.CharField(max_length=16)),
                ('third_name', models.CharField(max_length=16)),
                ('third_id', models.CharField(max_length=16)),
                ('password', models.CharField(max_length=16)),
                ('avatar_url', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VerfyModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('phone', models.CharField(max_length=16)),
                ('code', models.IntegerField()),
                ('createdate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('stage', models.IntegerField()),
                ('question_id', models.IntegerField()),
                ('score', models.IntegerField()),
                ('roleid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.roleinfo')),
            ],
        ),
        migrations.AddField(
            model_name='roleinfo',
            name='userid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.userinfo'),
        ),
    ]