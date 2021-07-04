# Generated by Django 3.2.5 on 2021-07-02 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_pet_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='photoUrls',
            field=models.URLField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='pet',
            name='tags',
            field=models.CharField(max_length=200),
        ),
    ]