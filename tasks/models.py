from django.db import models

class Task(models.Model):
    owner = models.CharField(max_length = 150)
    name = models.CharField(max_length = 150)
    task_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    
    
