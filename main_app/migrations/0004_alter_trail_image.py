# Generated by Django 5.2.1 on 2025-06-10 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_trail_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trail',
            name='image',
            field=models.ImageField(default='cover_image_1.jpg', upload_to='cover_image/'),
        ),
    ]
