# Generated by Django 4.0.2 on 2022-04-09 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeranker', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuploadfile',
            name='text',
            field=models.TextField(null=True),
        ),
    ]
