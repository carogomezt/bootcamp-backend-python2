from django.shortcuts import render

# Create your views here.
from django.views import View
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Document
from .utils import generate_custom_presigned_url
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name="dispatch")
class UploadDocumentView(View):
    def post(self, request):
        file = request.FILES.get("file")
        title = request.POST.get("title")

        if not file or not title:
            return JsonResponse({"error": "File and title are required"}, status=400)

        document = Document.objects.create(title=title, file=file)
        file_url = generate_custom_presigned_url(document.file.name)
        return JsonResponse(
            {
                "id": document.id,
                "title": document.title,
                "file_url": file_url,
                "uploaded_at": document.uploaded_at,
            },
            status=201,
        )


class ListDocumentsView(View):
    def get(self, request):
        documents = Document.objects.all()
        data = []
        for doc in documents:
            file_url = generate_custom_presigned_url(doc.file.name)
            data.append(
                {
                    "id": doc.id,
                    "title": doc.title,
                    "original_url": doc.file.url,
                    "file_url": file_url,
                    "uploaded_at": doc.uploaded_at,
                }
            )
        return JsonResponse(data, safe=False)


class DownloadDocumentView(View):
    def get(self, request, id):
        document = get_object_or_404(Document, id=id)
        file_url = generate_custom_presigned_url(document.file.name)
        if not file_url:
            return JsonResponse({"error": "Could not generate URL"}, status=500)
        return JsonResponse({"url": file_url})


@method_decorator(csrf_exempt, name="dispatch")
class DeleteDocumentView(View):
    def delete(self, request, id):
        document = get_object_or_404(Document, id=id)
        document.file.delete(save=False)  # Delete from S3
        document.delete()  # Delete DB entry
        return JsonResponse({"message": "Document deleted"})
