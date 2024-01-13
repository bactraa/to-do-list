# Generated by Django 5.0.1 on 2024-01-13 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('notes', models.TextField(blank=True, null=True)),
                ('deadline', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('NEW', 'NEW'), ('PROCESSING', 'PROCESSING'), ('FINISHED', 'FINISHED'), ('UNFINISHED', 'UNFINISHED')], default='NEW', max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
