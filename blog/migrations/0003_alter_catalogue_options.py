# Generated by Django 3.2 on 2022-03-19 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20220305_1123'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='catalogue',
            options={'ordering': ('note', 'level', 'order'), 'verbose_name': '笔记目录', 'verbose_name_plural': '笔记目录'},
        ),
    ]