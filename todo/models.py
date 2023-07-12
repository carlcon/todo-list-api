from django.db import models

class Todo(models.Model):
    text = models.CharField(max_length=1000, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)

    
