from django.db import models
from django.urls import reverse

class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    url = models.CharField(max_length=200, null=True, blank=True)
    named_url = models.CharField(max_length=100, null=True, blank=True)

    def get_absolute_url(self):
        if self.url:
            return self.url
        elif self.named_url:
            return reverse(self.named_url)
        else:
            return '#'