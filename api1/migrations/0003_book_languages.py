# Generated by Django 4.2.7 on 2023-11-16 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api1', '0002_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='languages',
            field=models.ManyToManyField(related_name='lang', to='api1.language'),
        ),
    ]