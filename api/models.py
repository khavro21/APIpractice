from django.db import models
from django.contrib.auth.models import User


# Creating a Pet
class Pet(models.Model):
    CATEGORY = (
        ('dog', 'dog'),
        ('cat', 'cat'),
        ('whale', 'whale'),
                )
    category = models.CharField(choices=CATEGORY, max_length=50)
    name = models.CharField(max_length=30)
    tags = models.CharField(max_length=200)
    status = models.BooleanField(default=True, verbose_name='Is Available')
    photoUrls = models.URLField(blank=True)
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
