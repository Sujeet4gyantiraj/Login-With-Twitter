from django.db import models


class Postfile(models.Model):
    tweet_post = models.CharField(max_length=100)