# Generated by Django 3.0.5 on 2020-07-01 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0007_auto_20200701_1709'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='answered',
        ),
        migrations.AddField(
            model_name='answered',
            name='answered_user',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
