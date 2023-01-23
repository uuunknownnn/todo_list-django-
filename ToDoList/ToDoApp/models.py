from django.db import models
from django.utils import timezone
#import datetime
from django.urls import reverse

# Create your models here.  timezone.now

class Todo(models.Model):
    title=models.CharField(max_length=350)
    content=models.TextField(default = 'No Content to Show!')
    complete=models.BooleanField(default=False)
    date_posted = models.DateTimeField(default=timezone.now )

    def __str__(self):
        return(self.title)


#overridding this method will redirect us to the detail template of the new task whenever created by the CreateView
    def get_absolute_url(self):
        return reverse('todo-detail', kwargs={'pk': self.pk})