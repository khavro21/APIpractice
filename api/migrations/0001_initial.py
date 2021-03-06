# Generated by Django 3.2.5 on 2021-07-02 17:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('dog', 'dog'), ('cat', 'cat'), ('whale', 'whale')], max_length=50)),
                ('name', models.CharField(max_length=30)),
                ('tags', models.CharField(max_length=200)),
                ('status', models.BooleanField(default=True)),
                ('photoUrls', models.URLField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('poster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
