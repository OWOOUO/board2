# Generated by Django 3.1.3 on 2021-12-15 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_auto_20211215_1107'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]