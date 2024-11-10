from django.db import models

class Login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    type = models.CharField(max_length=30)

class User(models.Model):
    LOGIN = models.ForeignKey(Login,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=30)
    dob = models.DateField()
    photo = models.FileField()
    email = models.CharField(max_length=50)
    phone = models.BigIntegerField()
    place = models.CharField(max_length=100)
    pin = models.BigIntegerField()
    post = models.CharField(max_length=100)

class News(models.Model):
    title = models.TextField()
    image_url = models.URLField()
    summary = models.TextField()
    Category = models.TextField()
    content = models.TextField()
    published_at = models.DateTimeField()
    source_url = models.URLField()


class Comment(models.Model):
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    NEWS = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments')
    comment_text = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True,null=True)


class Notification(models.Model):
    notification=models.CharField(max_length=1000)
    date=models.DateField()

