# Generated by Django 3.1.3 on 2020-11-29 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0002_auto_20201127_2141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainline',
            name='endplaceseq',
        ),
        migrations.RemoveField(
            model_name='trainline',
            name='startplaceseq',
        ),
        migrations.AddField(
            model_name='ticketkind',
            name='endplaceseq',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ticketkind',
            name='startplaceseq',
            field=models.IntegerField(default=0),
        ),
    ]
