# Generated by Django 5.0.3 on 2024-05-09 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Studentlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Stu_Name', models.CharField(max_length=100)),
                ('Stu_Class', models.IntegerField(max_length=10)),
                ('Stu_Email', models.EmailField(max_length=254)),
            ],
        ),
    ]