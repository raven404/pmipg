from datetime import datetime
from django.db import models
from django.contrib.auth import get_user_model
from tinymce.models import HTMLField
from django.urls import reverse
from posts.models import Author
User = get_user_model()
# Create your models here.


# class Author(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     profile_picture = models.ImageField()

#     def __str__(self):
#         return self.user.username


class NewsView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    news = models.ForeignKey('News', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


# class Comment(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     timestamp = models.DateTimeField(auto_now_add=True)
#     content = models.TextField()
#     post = models.ForeignKey(
#         'Post', related_name='comments', on_delete=models.CASCADE)

#     def __str__(self):
#         return self.user.username


class News(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    date = models.DateField(null=True, blank=True)
    content = HTMLField()
    comment_count = models.IntegerField(default=0)
    view_count = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField()
    slider = models.BooleanField()
    previous_post = models.ForeignKey(
        'self', related_name='previous', on_delete=models.SET_NULL, blank=True, null=True)
    next_post = models.ForeignKey(
        'self', related_name='next', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts:post-detail', kwargs={
            'pk': self.pk
        })

    def get_update_url(self):
        return reverse('posts:post-update', kwargs={
            'pk': self.pk
        })

    def get_delete_url(self):
        return reverse('posts:post-delete', kwargs={
            'pk': self.pk
        })

    @property
    def view_count(self):
        return PostView.objects.filter(post=self).count()


class video(models.Model):
    title = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    date = models.DateField(null=True, blank=True)
    featured = models.BooleanField(default=True)
    slider = models.BooleanField(default=False)
    video = models.FileField(upload_to='videos/')

    class Meta:
        verbose_name = 'video'
        verbose_name_plural = 'videos'

    def __str__(self):
        return self.title
