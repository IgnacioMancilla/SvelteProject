from django.db import models

class Slide(models.Model):
    image = models.ImageField(upload_to='slides/')
    alt = models.CharField(max_length=160, blank=True)
    caption = models.CharField(max_length=160, blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-updated']

    def __str__(self):
        return self.alt or f"Slide {self.pk}"
