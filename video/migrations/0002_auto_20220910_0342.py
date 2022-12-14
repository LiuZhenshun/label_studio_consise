# Generated by Django 3.2.6 on 2022-09-10 03:42

from django.db import migrations, models
import video.models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='frame_num',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='video',
            name='filename',
            field=models.FileField(max_length=128, upload_to=video.models.user_directory_path),
        ),
    ]
