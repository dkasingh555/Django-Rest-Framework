# Generated by Django 5.0.6 on 2024-05-20 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0002_studentlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentlist',
            name='Stu_Fee',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='studentlist',
            name='Stu_Fname',
            field=models.CharField(default='Default Value', max_length=100),
        ),
        migrations.AlterField(
            model_name='studentlist',
            name='Stu_Class',
            field=models.IntegerField(),
        ),
    ]
