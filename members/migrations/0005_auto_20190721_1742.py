# Generated by Django 2.2.2 on 2019-07-21 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_member_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='profile',
            field=models.ImageField(blank=True, upload_to='static/members'),
        ),
    ]
