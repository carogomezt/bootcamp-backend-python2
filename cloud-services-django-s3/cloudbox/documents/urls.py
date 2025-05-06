from django.urls import path
from .views import (
    UploadDocumentView,
    ListDocumentsView,
    DownloadDocumentView,
    DeleteDocumentView,
)

urlpatterns = [
    path("upload/", UploadDocumentView.as_view(), name="upload-document"),
    path("list/", ListDocumentsView.as_view(), name="list-documents"),
    path(
        "download/<int:id>/", DownloadDocumentView.as_view(), name="download-document"
    ),
    path("delete/<int:id>/", DeleteDocumentView.as_view(), name="delete-document"),
]
