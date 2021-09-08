# Generated by Django 3.2 on 2021-08-27 10:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Competency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.RenameField(
            model_name='activity',
            old_name='url',
            new_name='host_url',
        ),
        migrations.AddField(
            model_name='activity',
            name='competencies',
            field=models.ManyToManyField(to='portfolio.Competency'),
        ),
        migrations.AddField(
            model_name='activity',
            name='languages',
            field=models.ManyToManyField(to='portfolio.Language'),
        ),
    ]
