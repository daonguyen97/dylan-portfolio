from django.db import models

class Page(models.Model):
    title = models.CharField(max_length=255, unique=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.BooleanField()

    def __str__(self):
        return self.title + '.html'

class NavbarItem(models.Model):
    label = models.CharField(max_length=50, unique=True)
    url_link = models.CharField(max_length=255)
    svg_image = models.TextField()
    status = models.BooleanField()

    class Meta:
        ordering = ['id']
        
    def __str__(self):
        return self.label
