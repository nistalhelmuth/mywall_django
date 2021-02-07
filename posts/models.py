from django.db import models
from django.utils import timezone

class Comment(models.Model):
    content = models.CharField(max_length = 280)
    created_by = models.ForeignKey(User, on_delete = models.DO_NOTHING) # check
    date_created = models.DateTimeField(default = timezone.now)
    date_modified = models.DateTimeField(null = True)

    def __str__(self):
        return ('%s-%s-%s') % self.created_by, self.date_created


class Post(models.Model):
    content = models.CharField(max_length = 280)
    # photo = models.CharField()
    created_by = models.ForeignKey(User, on_delete = models.DO_NOTHING) # check
    date_created = models.DateTimeField(default = timezone.now)
    date_modified = models.DateTimeField(null = True)
    comments = models.ManyToManyField(Comment, on_delete = models.CASCADE)

    def __str__(self):
        return ('%s-%s-%s') % self.created_by, self.date_created

    