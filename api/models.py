from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.urls.resolvers import re


class Profile(models.Model):
     user = models.OneToOneField(User, on_delete=models.CASCADE)
     county = models.CharField(max_length=200)
     association = models.CharField(max_length=200)

     def __str__(self):
            return str(self.user)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question


class Choice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    

    def __str__(self):
        return f"{self.question}-{self.user}-{self.choice}"



class Forum(models.Model):
    username = models.CharField(max_length=255)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created     = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-created',)
   
    def __str__(self):
        return self.title

class ForumComment(models.Model):
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    username = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField()
    created  = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.comment[:20]

class ForumVote(models.Model):
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    username = models.CharField(max_length=255, blank=True, null=True)
    up_vote = models.PositiveIntegerField()
    down_vote = models.PositiveIntegerField()

    def __str__(self):
        return self.username

   





