# Generated by Django 3.2 on 2021-04-20 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('python_serv', '0003_auto_20210420_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaldata',
            name='group',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='personaldata',
            name='name',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='personaldata',
            name='surname',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='personaldata',
            name='uid',
            field=models.CharField(max_length=32),
        ),
    ]