# Generated by Django 4.2.7 on 2023-12-05 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_remove_booking_courses_booking_courses'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='booked_courses',
            field=models.ManyToManyField(blank=True, to='courses.course'),
        ),
    ]
