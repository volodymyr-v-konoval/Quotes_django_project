import uuid
from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.

class Author(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fullname = models.CharField(max_length=75, null=False, unique=True)
    born_date = models.CharField(max_length=25, null=False)
    born_location = models.CharField(max_length=100, null=False)
    description = models.TextField()

    def __str__(self):
        return f"{self.fullname}"

class Quote(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = ArrayField(models.CharField(max_length=100), blank=True, default=list)
    quote = models.TextField()

    def __str__(self):
        return f"{self.quote}"