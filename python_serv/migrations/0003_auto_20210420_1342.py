# Generated by Django 3.2 on 2021-04-20 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('python_serv', '0002_auto_20210420_1246'),
    ]

    operations = [
        migrations.AddField(
            model_name='personaldata',
            name='group',
            field=models.TextField(default=123),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personaldata',
            name='name',
            field=models.TextField(default=123),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personaldata',
            name='surname',
            field=models.TextField(default=123),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personaldata',
            name='uid',
            field=models.TextField(default=123),
            preserve_default=False,
        ),
    ]
