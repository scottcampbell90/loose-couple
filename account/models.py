from django.db import models
from django.contrib.auth.models import User


class PostModel(models.Model):

    title = models.CharField(
        max_length=50
    )

    body = models.CharField(
        max_length=500
    )

    date = models.DateTimeField(
        auto_now_add=True
    )

    user = models.ForeignKey(
        User,
        blank=True,
        null=True,
        related_name='posts'
    )

    class Meta:
        ordering = ['-date']
        app_label = 'account'

    def __unicode__(self):
        return self.title


class Channel(models.Model):

    name = models.CharField(
        max_length=50
    )

    detail = models.CharField(
        max_length=100
    )

    created_on = models.DateTimeField(
        auto_now_add=True,
        auto_now=False
    )

    creator = models.ForeignKey(
        User,
        blank=True,
        null=True,
        related_name='channels'
    )

    members = models.ManyToManyField(
        User,
        related_name='members',
        symmetrical=False
    )

    class Meta:
        ordering = ['-created_on']
        app_label = 'account'

    def __unicode__(self):
        return self.name


class UserProfile(models.Model):

    user = models.ForeignKey(
        User,
        unique=True,
        related_name='user'
    )

    channels = models.ManyToManyField(
        Channel,
        related_name='channels',
        symmetrical=False
    )

    follows = models.ManyToManyField(
        User,
        related_name='follows',
        symmetrical=False
    )

    def __unicode__(self):
        return self.user.username + "'s profile"
