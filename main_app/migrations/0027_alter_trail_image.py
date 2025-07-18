# Generated by Django 5.2.1 on 2025-06-15 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0026_alter_trail_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trail',
            name='image',
            field=models.CharField(choices=[('cover_image_1.jpg', 'Image 1'), ('cover_image_2.jpg', 'Image 2'), ('cover_image_3.jpg', 'Image 3'), ('cover_image_4.jpg', 'Image 4'), ('cover_image_5.jpg', 'Image 5'), ('cover_image_6.jpg', 'Image 6'), ('cover_image_7.jpg', 'Image 7'), ('cover_image_8.jpg', 'Image 8'), ('cover_image_10.jpg', 'Image 10')], max_length=100, verbose_name='Cover Image'),
        ),
    ]
