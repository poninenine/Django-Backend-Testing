# Generated by Django 4.1.3 on 2023-01-26 23:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dj_test_app', '0012_remove_image_album'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='album',
        ),
        migrations.AddField(
            model_name='image',
            name='album',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='dj_test_app.imagealbum'),
        ),
    ]
