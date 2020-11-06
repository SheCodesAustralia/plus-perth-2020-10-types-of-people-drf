# Generated by Django 3.0.8 on 2020-11-05 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_mentorprofile_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentorprofile',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True),
        ),
        migrations.AddField(
            model_name='mentorprofile',
            name='location',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='mentorprofile',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True),
        ),
    ]
