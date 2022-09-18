from datetime import datetime

from django.db import models


class Stage(models.Model):
    title = models.TextField()
    estimated = models.DateTimeField()
    actual = models.DateTimeField(default=datetime.now)

    def key(self):
        return self.actual

    def __str__(self):
        return f"{{id={self.id}, title={self.title}, estimated={self.estimated}, actual={self.actual}}}"


class Task(models.Model):
    title = models.TextField()
    head = models.DateTimeField(default=datetime.now)
    tail = models.DateTimeField(null=True, default=None)
    estimated = models.DurationField()
    actual = models.DurationField(null=True, default=None)
    state = models.IntegerField(default=0)

    def key(self):
        return self.head

    def __str__(self):
        return f"{{id={self.id}, title={self.title}, head={self.head}, tail={self.tail}, estimated={self.estimated}, actual={self.actual}, state={self.state}}}"


class Comment(models.Model):
    name = models.TextField()
    content = models.TextField()
    moment = models.DateTimeField(default=datetime.now)

    def key(self):
        return self.moment

    def __str__(self):
        return f"{{id={self.id}, name={self.name}, content={self.content}, moment={self.moment}}}"


class Plan(models.Model):
    title = models.TextField()
    clock = models.TimeField()
    day = models.IntegerField(default=7)

    def __str__(self):
        return f"{{id={self.id}, title={self.title}, clock={self.clock}, day={self.day}}}"


class Record(models.Model):
    moment = models.DateTimeField(default=datetime.now)
    ip = models.TextField(default="xxx.xxx.xxx.xxx")
    token = models.TextField()

    def __str__(self):
        return f"{{id={self.id}, moment={self.moment}, ip={self.ip}, token={self.token}}}"
