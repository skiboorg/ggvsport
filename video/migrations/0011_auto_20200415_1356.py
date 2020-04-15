# Generated by Django 3.0.5 on 2020-04-15 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0010_auto_20200415_1215'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='duration',
            field=models.IntegerField(default=0, verbose_name='Длительность'),
        ),
        migrations.AddField(
            model_name='video',
            name='is_now_watching',
            field=models.BooleanField(default=False, verbose_name='Смотрят?'),
        ),
        migrations.AddField(
            model_name='video',
            name='start_watch',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
