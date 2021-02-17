# Generated by Django 3.1.3 on 2020-11-29 22:03

from django.db import migrations, models
import django.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0002_user_phonenum'),
        ('ticket', '0004_ticketkind_trainline'),
    ]

    operations = [
        migrations.CreateModel(
            name='TicketOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticketid', models.ForeignKey(on_delete=django.db.models.fields.DateField, to='ticket.ticketkind')),
                ('userid', models.ForeignKey(on_delete=django.db.models.fields.DateField, to='userinfo.user')),
            ],
        ),
    ]
