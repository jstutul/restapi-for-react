# Generated by Django 4.0.2 on 2022-02-07 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='images',
            field=models.ImageField(default='default.jpg', upload_to='student/'),
        ),
    ]
