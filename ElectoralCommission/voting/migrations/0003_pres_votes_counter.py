# Generated by Django 2.1.3 on 2019-01-10 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0002_parliamentary_presidential'),
    ]

    operations = [
        migrations.CreateModel(
            name='pres_votes_counter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'Presidential_votes_counter',
            },
        ),
    ]
