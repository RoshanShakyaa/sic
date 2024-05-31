# Generated by Django 5.0.6 on 2024-05-31 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0002_noitce'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('desc', models.TextField()),
                ('attachment', models.FileField(blank=True, null=True, upload_to='notices')),
                ('created', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Noitce',
        ),
    ]