from datetime import timedelta
from django.db import models
from django.utils import timezone

# Create your models here.

def default_duedate():
	return timedelta(days=1) + timezone.now()



class Todo(models.Model):
	name = models.CharField(max_length=255, unique=True)
	is_completed = models.BooleanField(db_index=True)
	notes = models.TextField(blank=True)
	due_date = models.DateTimeField(default=default_duedate)
