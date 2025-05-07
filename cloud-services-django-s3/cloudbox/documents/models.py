from uuid import uuid4
from django.db import models


# Create your models here.


class Document(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(
        max_length=100,
        upload_to="documents",
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
