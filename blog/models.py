from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=400)
    bio = models.TextField()
    subject = models.CharField(max_length=300)
    email = models.TextField()
    img = models.ImageField(upload_to='category/')

    def __str__(self):
        return self.name



class Contact(models.Model):
    name = models.CharField(max_length=400)
    message = models.TextField()
    subject = models.CharField(max_length=300)
    email = models.TextField()

    def __str__(self):
        return self.name


class Index(models.Model):
    name = models.CharField(max_length=400)
    bio = models.TextField()
    subject = models.CharField(max_length=300)
    email = models.TextField()

    def __str__(self):
        return self.name


class Single(models.Model):
    name = models.CharField(max_length=400)
    bio = models.TextField()
    subject = models.CharField(max_length=300)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Feature(models.Model):
    name = models.CharField(max_length=400)
    date = models.DateField(auto_now=True)
    img = models.ImageField(upload_to='feature/')
    status = models.CharField(max_length=300)
    slug = models.SlugField(max_length=400)
    def __str__(self):
        return self.name
class Newsletter(models.Model):
    email = models.EmailField(max_length=300)
    def __str__(self):
        return self.email

class LatestNews(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    img = models.ImageField(upload_to='latestNews/')
    status = models.CharField(max_length=99)
    bio = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Biz(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='biz/')
    status = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    def __str__(self):
        return self.name

class Sen(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='biz/')
    status = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    def __str__(self):
        return self.name

class Lorem(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField(auto_now=True)
    status = models.CharField(max_length=200)

class Tranding(models.Model):
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    date = models.DateField(auto_now=True)
    def __str__(self):
        return self.name

class Newsletter(models.Model):
    email = models.EmailField(max_length=300)
    def __str__(self):
        return self.email

class Image(models.Model):
    name = models.CharField(max_length=300)
    img = models.ImageField(upload_to='image/')
    def __str__(self):
        return self.name

class Busin(models.Model):
    name = models.CharField(max_length=600)
    status = models.CharField(max_length=700)
    date = models.DateField(auto_now=True)
    image = models.ImageField(upload_to='busin/')
    def __str__(self):
        return self.name


class Picture(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='picture/')
    status = models.CharField(max_length=200)
    date = models.DateField(auto_now=True)
    def __str__(self):
        return self.name

class Sit(models.Model):
    name = models.CharField(max_length=300)
    status = models.CharField(max_length=200)
    date = models.DateField(auto_now=True)
    def __str__(self):
        return self.name

class Ipsum(models.Model):
    name = models.CharField(max_length=700)
    status = models.CharField(max_length=9000)
    date = models.DateField(auto_now=True)
    image = models.ImageField(upload_to='ipsum/')
    def __str__(self):
        return self.name


class Newsletter(models.Model):
    email = models.EmailField(max_length=300)
    def __str__(self):
        return self.email
