from django.contrib import admin
from django.utils.html import format_html
from .models import Document
from .utils import generate_custom_presigned_url


# Register your models here.
class DocumentAdmin(admin.ModelAdmin):
    list_display = ("title", "file_link")

    def file_link(self, obj):
        if obj.file:
            url = generate_custom_presigned_url(obj.file.name)
            return format_html('<a href="{}" target="_blank">Download</a>', url)
        return "-"

    file_link.short_description = "File URL"


admin.site.register(Document, DocumentAdmin)
