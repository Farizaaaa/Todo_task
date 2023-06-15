from django.contrib import admin



# Register your models here.
from . models import Task

admin.site.register(Task)


def __str__(self):
    return self.name

