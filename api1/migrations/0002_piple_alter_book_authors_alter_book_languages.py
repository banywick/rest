# Generated by Django 4.2.7 on 2023-11-21 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Piple',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('old', models.IntegerField()),
                ('sex', models.CharField(default='m', max_length=1)),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='authors',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='aut', to='api1.author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='languages',
            field=models.ManyToManyField(related_name='lan', to='api1.language'),
        ),
    ]