from django.contrib.auth.models import User
from django.urls import reverse
from django.db import models


class Category(models.Model):
    objects = None
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/post_images", null=True)
    description = models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='blog_posts')
    category = models.CharField(max_length=200, default='uncategorized')

    class Meta:
        ordering = ['-posted_on']

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + '|' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(blank=True, null=True, upload_to="images/profile_pics")
    instagram_url = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('home')


class PostComments(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    comment = models.TextField()
    commented_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-commented_on']

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)
