# Generated by Django 2.2.6 on 2019-10-18 18:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Insta', '0002_userconnection'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='posted_on',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2019, 10, 18, 18, 10, 7, 589907, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
