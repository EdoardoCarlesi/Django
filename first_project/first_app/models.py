from django.db import models


class Topic(models.Model):

    topic_name = models.CharField(max_length=128, unique=True)
    
    def __str__(self):
        return self.topic_name


class WebPage(models.Model):

    topic = models.ForeignKey(Topic, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=64, unique=True)
    url = models.URLField(unique=True)


    def __str__(self):
        return self.name


class AccessRecord(models.Model):

    name = models.ForeignKey(WebPage, on_delete=models.DO_NOTHING)
    date = models.DateField()

    def __str__(self):
        return str(self.date)


class User(models.Model):

    first_name = models.CharField(max_length=64, unique=True)
    last_name = models.CharField(max_length=64, unique=True)
    email = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.first_name

