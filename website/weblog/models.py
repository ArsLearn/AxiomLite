from django.db import models as m
from django.conf import settings as s
from django.utils import timezone


class Tag(m.Model):
    name = m.CharField(max_length = 64)


    def __str__(self):
        return self.name


class Post(m.Model):


    STATUS_CHOICES = {
        "draft": "Draft",
        "published": "Published"
    }

    MODE_CHOICES = {
        "created": "Created",
        "edited": "Edited",
        "deleted": "Deleted",
        "banned": "Banned"
    }


    title = m.CharField(max_length = 128)
    text = m.TextField()
    slug = m.SlugField(max_length = 256, unique = True)
    author = m.ForeignKey(s.AUTH_USER_MODEL, on_delete = m.CASCADE, related_name = "posts")
    created = m.DateTimeField(auto_now_add = True)
    published = m.DateTimeField(default = timezone.now)
    updated = m.DateTimeField(auto_now = True)
    status = m.CharField(max_length = 64, choices = STATUS_CHOICES, default = "draft")
    mode = m.CharField(max_length = 64, choices = MODE_CHOICES, default = "created")
    tag = m.ManyToManyField(Tag, related_name = "tags")


    def __str__(self):
        return self.title
    

class Comment(m.Model):


    user = m.ForeignKey(s.AUTH_USER_MODEL, on_delete = m.CASCADE, null = True, related_name = "comments")
    post = m.ForeignKey(Post, on_delete = m.CASCADE, related_name = "comments")
    text = m.TextField()


    def __str__(self):
        return f"@{self.user.username} Comment On {self.post.title}"


class Like(m.Model):


    user = m.ForeignKey(s.AUTH_USER_MODEL, on_delete = m.CASCADE, related_name = "likes")
    post = m.ForeignKey(Post, on_delete = m.CASCADE, related_name = "likes")
    liked = m.DateTimeField(auto_now_add = True)


    class Meta:
        unique_together = ["user", "post"]


    def __str__(self):
        return f"@{self.user.username} Liked {self.post.title}"
