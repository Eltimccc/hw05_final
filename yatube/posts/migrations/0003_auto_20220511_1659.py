# Generated by Django 2.2.19 on 2022-05-11 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20220511_1045'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='url',
            new_name='slug',
        ),
        migrations.AlterField(
            model_name='group',
            name='description',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='group',
            name='title',
            field=models.CharField(max_length=150),
        ),
    ]
