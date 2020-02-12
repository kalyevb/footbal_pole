# Generated by Django 2.2.8 on 2019-12-10 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fieldsapp', '0003_pole_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='pole',
            name='email',
            field=models.CharField(default=1, max_length=50, verbose_name='Email'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pole',
            name='number',
            field=models.CharField(default=1, max_length=20, verbose_name='Номер'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pole',
            name='avatar',
            field=models.ImageField(upload_to='', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='pole',
            name='body',
            field=models.TextField(verbose_name='Описание поля'),
        ),
        migrations.AlterField(
            model_name='pole',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Название поля'),
        ),
    ]