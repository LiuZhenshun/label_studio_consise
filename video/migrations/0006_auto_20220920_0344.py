# Generated by Django 3.2.6 on 2022-09-20 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0005_alter_video_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='frame_num',
        ),
        migrations.AddField(
            model_name='video',
            name='video_info',
            field=models.JSONField(default={}, null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='data',
            field=models.JSONField(default={}, null=True),
        ),
    ]
