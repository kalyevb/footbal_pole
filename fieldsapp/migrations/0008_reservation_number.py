# Generated by Django 2.2.8 on 2019-12-13 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fieldsapp', '0007_auto_20191213_1953'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='number',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
