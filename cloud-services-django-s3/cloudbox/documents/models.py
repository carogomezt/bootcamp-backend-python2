from uuid import uuid4
from django.db import models
from storages.backends.s3 import S3File
from storages.backends.s3boto3 import S3Boto3Storage
from .utils import get_document_s3_file_path


# Create your models here.


class DocumentFileS3Storage(S3Boto3Storage):
    location = "documents"


class Document(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(
        max_length=100,
        storage=DocumentFileS3Storage,
        upload_to=get_document_s3_file_path,
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def open(self) -> S3File:
        storage = DocumentFileS3Storage()
        return storage.open(self.file.name, mode="rb")

    def __str__(self):
        return self.title
