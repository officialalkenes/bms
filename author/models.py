from django.db import models
from django.contrib.auth.models import User

from django.utils.text import slugify

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pics = models.ImageField(upload_to="author_profile_pics")
    pseudonym = models.CharField(max_length=100, unique=True) # My boy
    slug = models.SlugField(max_length=100, blank=True) # my-boy
    website = models.URLField(blank=True)

    def __str__(self) -> str:
        return f'{self.pseudonym}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.pseudonym)
        return super().save(*args, **kwargs)