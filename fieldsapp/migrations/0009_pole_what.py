# Generated by Django 2.2.8 on 2019-12-13 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fieldsapp', '0008_reservation_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='pole',
            name='what',
            field=models.CharField(default=1, max_length=10, verbose_name='Поле'),
            preserve_default=False,
        ),
    ]
