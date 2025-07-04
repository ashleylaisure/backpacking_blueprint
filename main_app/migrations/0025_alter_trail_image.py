# Generated by Django 5.2.1 on 2025-06-15 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0024_alter_trail_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trail',
            name='image',
            field=models.CharField(blank=True, choices=[('/cover_photos/cover_image_1.jpg', 'Imgae 1'), ('/cover_photos/cover_image_2.jpg', 'Imgae 2'), ('/cover_photos/cover_image_3.jpg', 'Imgae 3'), ('/cover_photos/cover_image_4.jpg', 'Imgae 4'), ('/cover_photos/cover_image_5.jpg', 'Imgae 5'), ('/cover_photos/cover_image_6.jpg', 'Imgae 6'), ('/cover_photos/cover_image_7.jpg', 'Imgae 7'), ('/cover_photos/cover_image_8.jpg', 'Imgae 8'), ('/cover_photos/cover_image_9.jpg', 'Imgae 9'), ('/cover_photos/cover_image_10.jpg', 'Imgae 10')], default='/cover_photos/cover_image_7.jpg', max_length=100, null=True),
        ),
    ]
