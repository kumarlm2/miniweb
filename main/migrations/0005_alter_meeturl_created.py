# Generated by Django 3.2.8 on 2021-10-28 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_meeturl_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeturl',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
