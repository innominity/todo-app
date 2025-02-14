# Generated by Django 5.1.3 on 2024-11-10 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(1, 'Active'), (2, 'Done')], default=1)),
            ],
            options={
                'verbose_name': 'TODO задача',
                'verbose_name_plural': 'TODO задачи',
                'ordering': ['-created_at'],
            },
        ),
    ]
