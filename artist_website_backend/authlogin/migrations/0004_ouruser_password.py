# Generated by Django 4.2 on 2023-04-11 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authlogin', '0003_ouruser'),
    ]

    operations = [
        migrations.AddField(
            model_name='ouruser',
            name='password',
            field=models.CharField(default='empty', max_length=150),
            preserve_default=False,
        ),
    ]
