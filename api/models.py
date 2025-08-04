from django.db import models
from django.utils.text import slugify


def upload_to(instance, filename):
    return "images/{filename}".format(filename=filename)


# Create your models here.
class Post(models.Model):
    CATEGORY_CHOICES = [
        ("tech", "Technology"),
        ("life", "Lifestyle"),
        ("edu", "Education"),
        ("news", "News"),
        ("health", "Health"),
        ("travel", "Travel"),
        ("food", "Food"),
        ("sports", "Sports"),
        ("finance", "Finance"),
        ("ent", "Entertainment"),
    ]

    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default="tech")
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to=upload_to, null=True, blank=True)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            unique_slug = self.slug
            counter = 1
            if Post.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{self.slug}-{counter}"
                counter += 1
            self.slug = unique_slug

        super().save(*args, **kwargs)
