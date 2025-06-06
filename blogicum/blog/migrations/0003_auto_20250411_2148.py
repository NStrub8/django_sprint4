# Generated by Django 3.2.16 on 2025-04-11 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20250402_1327'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': (
                '-pub_date',), 'verbose_name': 'публикация', 'verbose_name_plural': 'Публикации'},
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, help_text='Прикрепите изображение к публикации.',
                                    null=True, upload_to='posts_image/', verbose_name='Изображение'),
        ),
    ]
