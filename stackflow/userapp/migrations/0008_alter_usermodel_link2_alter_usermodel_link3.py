# Generated by Django 4.2.5 on 2023-10-11 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0007_rename_link_usermodel_link3_usermodel_link1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='link2',
            field=models.URLField(blank=True, default='Link Bulunamadı', null=True, verbose_name='Website'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='link3',
            field=models.URLField(blank=True, default='Link Bulunamadı', null=True, verbose_name='Twitter'),
        ),
    ]
