# Generated by Django 4.2.1 on 2023-05-11 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('human', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MarriageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start', models.DateField()),
                ('date_end', models.DateField()),
                ('couple', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='human.humanmodel')),
            ],
        ),
    ]
