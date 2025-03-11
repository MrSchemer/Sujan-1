from django.db import models
from tinymce.models import HTMLField
# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=200)
    Hindi = models.IntegerField( default=60)
    English = models.IntegerField(default=90)
    Nepali = models.IntegerField(default=95)
    Skills = HTMLField(default='')
    tagline = models.CharField(max_length=200, default='Author, Researcher & Agriculturist')
    content = HTMLField()
    image = models.ImageField(upload_to='static/images/about/', null=True, blank=True)

    def __str__(self):
        return self.title

class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = HTMLField()
    image = models.ImageField(upload_to='static/images/blog/', null=True, blank=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200, default='')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Research(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = HTMLField()
    image = models.ImageField(upload_to='static/images/research/', null=True, blank=True)
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Publication(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = HTMLField()
    image = models.ImageField(upload_to='static/images/publication/', null=True, blank=True)
    publisher = models.CharField(max_length=200)
    published = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Organization_involved(models.Model):
    id = models.AutoField(primary_key=True)
    organization = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    description = HTMLField()
    started_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    image = models.ImageField(upload_to='static/images/organization/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.organization

class Honor(models.Model):
    id = models.AutoField(primary_key=True)
    organization = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    image = models.ImageField(upload_to='static/images/honor/', null=True, blank=True)
    description = HTMLField()
    created_at = models.DateField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.organization
