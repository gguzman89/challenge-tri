# Generated by Django 3.0.2 on 2020-01-14 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20200111_1613'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='people',
            name='courses',
        ),
        migrations.AddField(
            model_name='people',
            name='courses',
            field=models.ManyToManyField(related_name='peoples', to='polls.Course'),
        ),
    ]