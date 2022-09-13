# Generated by Django 3.2.6 on 2022-09-13 06:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountInfo',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('createdate', models.DateTimeField(auto_now_add=True)),
                ('updatedate', models.DateTimeField(auto_now=True)),
                ('username', models.CharField(max_length=16)),
                ('third_id', models.CharField(max_length=16)),
                ('password', models.CharField(max_length=16)),
                ('avatar_url', models.CharField(blank=True, max_length=255, null=True)),
                ('country', models.CharField(blank=True, max_length=32, null=True)),
                ('province', models.CharField(blank=True, max_length=32, null=True)),
                ('city', models.CharField(blank=True, max_length=32, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=128, null=True)),
                ('text', models.CharField(blank=True, max_length=1024, null=True)),
                ('enable', models.BooleanField(blank=True, null=True)),
                ('createdate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='GameKind',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('desc', models.CharField(blank=True, max_length=64, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RoleInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('last_game_kind', models.IntegerField(blank=True, null=True)),
                ('last_stage', models.IntegerField(blank=True, null=True)),
                ('last_step_id', models.IntegerField(blank=True, null=True)),
                ('updatedate', models.DateTimeField(auto_now=True)),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.accountinfo')),
            ],
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('gameKind', models.IntegerField()),
                ('desc', models.CharField(blank=True, max_length=64, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('stage', models.IntegerField()),
                ('stepMode', models.IntegerField()),
                ('topic', models.CharField(blank=True, max_length=128, null=True)),
                ('describtion', models.CharField(blank=True, max_length=255, null=True)),
                ('tips', models.CharField(blank=True, max_length=255, null=True)),
                ('qtype', models.IntegerField(blank=True, null=True)),
                ('skip', models.BooleanField(blank=True, null=True)),
                ('correct_score', models.IntegerField(blank=True, null=True)),
                ('uncorrect_score', models.IntegerField(blank=True, null=True)),
                ('op_1', models.CharField(blank=True, max_length=255, null=True)),
                ('op_2', models.CharField(blank=True, max_length=255, null=True)),
                ('op_3', models.CharField(blank=True, max_length=255, null=True)),
                ('op_4', models.CharField(blank=True, max_length=255, null=True)),
                ('correct', models.CharField(blank=True, max_length=16, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StepMode',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('mode', models.IntegerField(blank=True, null=True)),
                ('desc', models.CharField(blank=True, max_length=64, null=True)),
            ],
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
                ('step_id', models.IntegerField(blank=True, null=True)),
                ('score', models.IntegerField(blank=True, null=True)),
                ('roleid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.roleinfo')),
            ],
        ),
    ]
